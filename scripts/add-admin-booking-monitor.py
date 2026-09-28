from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/server/marketplaceApi.ts')
s=p.read_text()
needle='''  app.get("/api/workers/:workerId/bookings", async (req, res) => { if (!await canAccessWorker(req, req.params.workerId)) return res.status(401).json({ error: "Approved worker login required" }); const collection = await bookings(); const rows = collection ? await collection.find({ workerId: req.params.workerId }).sort({ createdAt: -1 }).toArray() : memoryBookings.filter((booking) => booking.workerId === req.params.workerId); return res.json(rows); });'''
insert=needle+'''\n  app.get("/api/admin/bookings", async (req, res) => { if (!await requireAdmin(req)) return res.status(401).json({ error: "Admin login required" }); const collection = await bookings(); const rows = collection ? await collection.find({}).sort({ createdAt: -1 }).toArray() : memoryBookings.slice().sort((a, b) => b.createdAt.localeCompare(a.createdAt)); return res.json(rows); });'''
if needle not in s: raise SystemExit('worker bookings route missing')
s=s.replace(needle,insert,1)
p.write_text(s)
