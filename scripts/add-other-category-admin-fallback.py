from pathlib import Path

signup = Path('/home/ubuntu/labrkp-workforce/client/src/pages/WorkerSignup.tsx')
s = signup.read_text()
s = s.replace('const skills = ["Electrical", "Plumbing", "Solar & Energy", "AC & Appliances", "Carpentry", "Cleaning", "Tailoring", "Tech & Electronics"];', 'const skills = ["Electrical", "Plumbing", "Solar & Energy", "AC & Appliances", "Carpentry", "Cleaning", "Tailoring", "Tech & Electronics", "Other"];')
s = s.replace('skill: "Electrical", experience:', 'skill: "Electrical", customSkill: "", experience:', 1)
s = s.replace('!form.name || !form.phone || !form.email || !form.experience', '!form.name || !form.phone || !form.email || !form.experience || (form.skill === "Other" && !form.customSkill)', 1)
s = s.replace('const response = await fetch("/api/workers/apply", {', 'const response = await fetch("/api/workers/apply", {', 1)
old = '<label className="mt-4 block"><span className="mb-2 block text-xs font-bold uppercase tracking-[0.13em] text-[#798780]">About your work *</span>'
new = '<label className="mt-4 block"><span className="mb-2 block text-xs font-bold uppercase tracking-[0.13em] text-[#798780]">Other category / service {form.skill === "Other" ? "*" : "(optional)"}</span><input value={form.customSkill} onChange={(e) => update("customSkill", e.target.value)} placeholder="e.g. Mobile repair, security, delivery..." className="w-full rounded-2xl border border-[#dbe4d9] px-4 py-3.5 text-sm outline-none focus:border-[#8aab62]" /></label>' + old
if old not in s: raise SystemExit('signup bio anchor missing')
s = s.replace(old, new, 1)
s = s.replace('<p className="mt-3 text-sm leading-6 text-[#65716e]">LABRKP team verification ke baad aapka profile KP workforce directory mein publish hoga.</p>', '<p className="mt-3 text-sm leading-6 text-[#65716e]">LABRKP team verification ke baad aapka profile KP workforce directory mein publish hoga. Admin panel mein request open karke Approve ya Reject karein.</p>', 1)
s = s.replace('Only KP cities are currently available on LABRKP.', 'Only KP cities are currently available on LABRKP. Other skills can be proposed and reviewed by admin.', 1)
signup.write_text(s)

api = Path('/home/ubuntu/labrkp-workforce/server/marketplaceApi.ts')
a = api.read_text()
a = a.replace('let db: Db | null = null;\n', 'let db: Db | null = null;\nconst memoryApplications: any[] = [];\n')
a = a.replace('if (database) await database.collection("workerApplications").insertOne(application);\n      return res.status(201).json({ application, persistence: database ? "mongodb" : "review-queue-fallback" });', 'if (database) await database.collection("workerApplications").insertOne(application); else memoryApplications.unshift(application);\n      return res.status(201).json({ application, persistence: database ? "mongodb" : "review-queue-fallback" });')
a = a.replace('app.get("/api/admin/worker-applications", async (_req, res) => { const database = await getDb(); if (!database) return res.json([]); return res.json(await database.collection("workerApplications").find({}).sort({ createdAt: -1 }).toArray()); });', 'app.get("/api/admin/worker-applications", async (_req, res) => { const database = await getDb(); if (!database) return res.json(memoryApplications); return res.json(await database.collection("workerApplications").find({}).sort({ createdAt: -1 }).toArray()); });')
old = 'app.patch("/api/admin/worker-applications/:id", async (req, res) => { const database = await getDb(); if (!database) return res.status(503).json({ error: "MongoDB is not configured" }); const result = await database.collection("workerApplications").findOneAndUpdate({ applicationId: req.params.id }, { $set: { status: req.body.status, reviewNote: req.body.reviewNote || "", reviewedAt: now(), updatedAt: now() } }, { returnDocument: "after" }); return result ? res.json(result) : res.status(404).json({ error: "Application not found" }); });'
new = 'app.patch("/api/admin/worker-applications/:id", async (req, res) => { const database = await getDb(); if (!database) { const item = memoryApplications.find((application) => application.applicationId === req.params.id); if (!item) return res.status(404).json({ error: "Application not found" }); Object.assign(item, { status: req.body.status, reviewNote: req.body.reviewNote || "", reviewedAt: now(), updatedAt: now() }); return res.json(item); } const result = await database.collection("workerApplications").findOneAndUpdate({ applicationId: req.params.id }, { $set: { status: req.body.status, reviewNote: req.body.reviewNote || "", reviewedAt: now(), updatedAt: now() } }, { returnDocument: "after" }); return result ? res.json(result) : res.status(404).json({ error: "Application not found" }); });'
if old not in a: raise SystemExit('approval endpoint missing')
a = a.replace(old, new, 1)
api.write_text(a)
