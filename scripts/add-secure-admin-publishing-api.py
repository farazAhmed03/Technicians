from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/server/marketplaceApi.ts')
s = p.read_text()
s = s.replace('import { storagePut } from "./storage";\n', 'import { storagePut } from "./storage";\nimport { sdk } from "./_core/sdk";\n')
s = s.replace('const memoryApplications: any[] = [];\n', 'const memoryApplications: any[] = [];\nconst memoryPublishedWorkers: any[] = [];\n')
anchor = 'function requireFields(body: any, fields: string[]) { return fields.filter((field) => !body?.[field] || (typeof body[field] === "string" && !body[field].trim())); }\n'
insert = anchor + '''async function requireAdmin(req: Request) {
  try { const user = await sdk.authenticateRequest(req); return user?.role === "admin" ? user : null; } catch { return null; }
}
function publicWorkerFromApplication(application: any) {
  return { id: application.applicationId, applicationId: application.applicationId, name: application.name, role: application.skill, city: `${application.city}, KPK`, experience: application.experience, rating: "New", reviews: 0, jobs: 0, price: "Contact", image: application.gender === "Female" ? "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=900&q=85" : "https://images.unsplash.com/photo-1621905252507-b35492cc74b4?auto=format&fit=crop&w=900&q=85", tags: [application.skill, "Verified newcomer", "KP local"], availability: "Newly approved", verified: true, accent: "#e7f3c7", bio: application.bio, gender: application.gender, services: [{ name: application.skill, duration: "Contact worker", price: "Contact" }], verification: { status: "Approved", reviewedAt: application.reviewedAt } };
}
'''
if anchor not in s: raise SystemExit('requireFields anchor missing')
s = s.replace(anchor, insert, 1)
# Replace admin GET/PATCH block.
start = '  app.get("/api/admin/worker-applications"'
end = '  app.get("/api/workers/:id/profile"'
i = s.index(start); j = s.index(end, i)
admin_block = '''  app.get("/api/admin/session", async (req, res) => { const user = await requireAdmin(req); return user ? res.json({ authenticated: true, user: { id: user.id, name: user.name, email: user.email, role: user.role } }) : res.status(401).json({ error: "Admin login required" }); });
  app.get("/api/admin/worker-applications", async (req, res) => { if (!await requireAdmin(req)) return res.status(401).json({ error: "Admin login required" }); const database = await getDb(); if (!database) return res.json(memoryApplications); return res.json(await database.collection("workerApplications").find({}).sort({ createdAt: -1 }).toArray()); });
  app.patch("/api/admin/worker-applications/:id", async (req, res) => { if (!await requireAdmin(req)) return res.status(401).json({ error: "Admin login required" }); const database = await getDb(); if (!database) { const item = memoryApplications.find((application) => application.applicationId === req.params.id); if (!item) return res.status(404).json({ error: "Application not found" }); Object.assign(item, { status: req.body.status, reviewNote: req.body.reviewNote || "", reviewedAt: now(), updatedAt: now() }); if (item.status === "Approved" && !memoryPublishedWorkers.some((worker) => worker.applicationId === item.applicationId)) memoryPublishedWorkers.unshift(publicWorkerFromApplication(item)); return res.json(item); } const result = await database.collection("workerApplications").findOneAndUpdate({ applicationId: req.params.id }, { $set: { status: req.body.status, reviewNote: req.body.reviewNote || "", reviewedAt: now(), updatedAt: now() } }, { returnDocument: "after" }); if (result && req.body.status === "Approved") await database.collection("publishedWorkers").updateOne({ applicationId: req.params.id }, { $set: publicWorkerFromApplication(result) }, { upsert: true }); return result ? res.json(result) : res.status(404).json({ error: "Application not found" }); });
  app.get("/api/workers/public", async (_req, res) => { const database = await getDb(); if (!database) return res.json(memoryPublishedWorkers); return res.json(await database.collection("publishedWorkers").find({}).sort({ reviewedAt: -1 }).toArray()); });
'''
s = s[:i] + admin_block + s[j:]
p.write_text(s)
