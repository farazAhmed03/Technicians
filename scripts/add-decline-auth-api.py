from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/server/marketplaceApi.ts')
s=p.read_text()
s=s.replace('"Completed" | "Cancelled";', '"Completed" | "Cancelled" | "Rejected";',1)
s=s.replace('async function requireSignedIn(req: Request) {\n  try { return await sdk.authenticateRequest(req); } catch { return null; }\n}', '''async function requireSignedIn(req: Request) {
  try { return await sdk.authenticateRequest(req); } catch { return null; }
}
async function canAccessWorker(req: Request, workerId: string) {
  const user = await requireSignedIn(req);
  if (!user) return null;
  if (user.role === "admin") return user;
  const database = await getDb();
  const worker = database ? await database.collection("publishedWorkers").findOne({ $or: [{ applicationId: workerId }, { id: workerId }] }) : null;
  return worker && ((worker as any).ownerOpenId === user.openId || (worker as any).email && (worker as any).email === user.email) ? user : null;
}''',1)
s=s.replace('app.get("/api/workers/:workerId/bookings", async (req, res) => { const collection', 'app.get("/api/workers/:workerId/bookings", async (req, res) => { if (!await canAccessWorker(req, req.params.workerId)) return res.status(401).json({ error: "Approved worker login required" }); const collection',1)
s=s.replace('app.post("/api/bookings/:id/accept", async (req, res) => {', 'app.post("/api/bookings/:id/accept", async (req, res) => {',1)
needle='''  app.post("/api/bookings/:id/location", async (req, res) => {'''
decline='''  app.post("/api/bookings/:id/decline", async (req, res) => { const collection = await bookings(); if (!collection) { const booking = memoryBookings.find((item) => item._id === req.params.id && item.status === "Pending"); if (!booking) return res.status(404).json({ error: "Pending booking not found" }); booking.status = "Rejected"; booking.rejectionReason = "Worker is unavailable for this request."; booking.customerNotification = "Your booking request was declined. Please choose another verified worker."; booking.updatedAt = now(); return res.json(booking); } const result = await collection.findOneAndUpdate({ _id: req.params.id, status: "Pending" }, { $set: { status: "Rejected", rejectionReason: "Worker is unavailable for this request.", customerNotification: "Your booking request was declined. Please choose another verified worker.", updatedAt: now() } }, { returnDocument: "after" }); return result ? res.json(result) : res.status(404).json({ error: "Pending booking not found" }); });
'''+needle
if needle not in s: raise SystemExit('location anchor missing')
s=s.replace(needle,decline,1)
s=s.replace('const application = { applicationId: createReference(), ...req.body,', 'const applicant = await requireSignedIn(req);\n      const application = { applicationId: createReference(), ownerOpenId: applicant?.openId, ...req.body,',1)
s=s.replace('if (result && req.body.status === "Approved") await database.collection("publishedWorkers").updateOne({ applicationId: req.params.id }, { $set: publicWorkerFromApplication(result) }, { upsert: true });', 'if (result && req.body.status === "Approved") await database.collection("publishedWorkers").updateOne({ applicationId: req.params.id }, { $set: { ...publicWorkerFromApplication(result), ownerOpenId: (result as any).ownerOpenId, email: (result as any).email } }, { upsert: true });',1)
p.write_text(s)
