from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/server/marketplaceApi.ts')
s = p.read_text()
s = s.replace('import { MongoClient, type Collection, type Db } from "mongodb";\n', 'import { MongoClient, type Collection, type Db } from "mongodb";\nimport { storagePut } from "./storage";\n')
s = s.replace('const application = { ...req.body, status: "Under Review", createdAt: now(), updatedAt: now() };', '''const documents: Record<string, { key: string; url: string; fileName: string; contentType: string }> = {};
      for (const field of ["diplomaProof", "skillProof"]) {
        const file = req.body[field];
        if (file?.data) {
          const content = String(file.data).split(",").pop() || "";
          const uploaded = await storagePut(`worker-applications/${String(req.body.email).replace(/[^a-z0-9]/gi, "-")}/${field}-${Date.now()}-${file.name || "proof"}`, Buffer.from(content, "base64"), file.type || "application/octet-stream");
          documents[field] = { ...uploaded, fileName: file.name || field, contentType: file.type || "application/octet-stream" };
        }
      }
      const application = { ...req.body, diplomaProof: undefined, skillProof: undefined, documents, status: "Under Review", createdAt: now(), updatedAt: now() };''')
needle = '  app.post("/api/bookings", async (req: Request, res: Response) => {'
insert = '''  app.get("/api/admin/worker-applications", async (_req, res) => { const database = await getDb(); if (!database) return res.json([]); return res.json(await database.collection("workerApplications").find({}).sort({ createdAt: -1 }).toArray()); });
  app.patch("/api/admin/worker-applications/:id", async (req, res) => { const database = await getDb(); if (!database) return res.status(503).json({ error: "MongoDB is not configured" }); const result = await database.collection("workerApplications").findOneAndUpdate({ _id: req.params.id }, { $set: { status: req.body.status, reviewNote: req.body.reviewNote || "", reviewedAt: now(), updatedAt: now() } }, { returnDocument: "after" }); return result ? res.json(result) : res.status(404).json({ error: "Application not found" }); });
  app.get("/api/workers/:id/profile", async (req, res) => { const database = await getDb(); const profile = database ? await database.collection("workerProfiles").findOne({ workerId: req.params.id }) : null; return profile ? res.json(profile) : res.status(404).json({ error: "Worker profile not found" }); });
  app.put("/api/workers/:id/profile", async (req, res) => { const database = await getDb(); if (!database) return res.status(503).json({ error: "MongoDB is not configured" }); const profile = { workerId: req.params.id, services: Array.isArray(req.body.services) ? req.body.services : [], availability: req.body.availability || "Available", serviceRadius: Number(req.body.serviceRadius || 25), updatedAt: now() }; await database.collection("workerProfiles").updateOne({ workerId: req.params.id }, { $set: profile }, { upsert: true }); return res.json(profile); });

'''
if needle not in s: raise SystemExit('booking endpoint anchor not found')
s = s.replace(needle, insert + needle, 1)
p.write_text(s)
