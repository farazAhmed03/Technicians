from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/server/marketplaceApi.ts')
s=p.read_text()
s=s.replace('app.post("/api/bookings/:id/accept", async (req, res) => { const collection', 'app.post("/api/bookings/:id/accept", async (req, res) => { if (!await canAccessWorker(req, String(req.body.workerId || ""))) return res.status(401).json({ error: "Approved worker login required" }); const collection',1)
s=s.replace('app.post("/api/bookings/:id/decline", async (req, res) => { const collection', 'app.post("/api/bookings/:id/decline", async (req, res) => { if (!await canAccessWorker(req, String(req.body.workerId || ""))) return res.status(401).json({ error: "Approved worker login required" }); const collection',1)
s=s.replace('app.post("/api/bookings/:id/location", async (req, res) => { const { lat, lng, accuracy }', 'app.post("/api/bookings/:id/location", async (req, res) => { if (!await canAccessWorker(req, String(req.body.workerId || ""))) return res.status(401).json({ error: "Approved worker login required" }); const { lat, lng, accuracy }',1)
p.write_text(s)

p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/WorkerConsole.tsx')
s=p.read_text()
s=s.replace('fetch(`/api/bookings/${pendingRequest._id}/accept`, { method: "POST" })', 'fetch(`/api/bookings/${pendingRequest._id}/accept`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ workerId }) })',1)
s=s.replace('fetch(`/api/bookings/${pendingRequest._id}/decline`, { method: "POST" })', 'fetch(`/api/bookings/${pendingRequest._id}/decline`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ workerId }) })',1)
s=s.replace('headers: { "Content-Type": "application/json" }, body: JSON.stringify({ lat:', 'headers: { "Content-Type": "application/json" }, body: JSON.stringify({ workerId, lat:',1)
p.write_text(s)
