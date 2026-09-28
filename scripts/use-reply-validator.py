from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/server/marketplaceApi.ts')
s=p.read_text().replace('if (!reply) return res.status(400).json({ error: "Reply text is required" });', 'if (!isValidReviewReply(reply)) return res.status(400).json({ error: "Reply text is required and must be 1–1000 characters" });', 1)
p.write_text(s)
