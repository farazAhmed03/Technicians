from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/server/marketplaceApi.ts')
s=p.read_text().replace('const nextStatus = String(req.body.status || ""); if (!allowed.includes(nextStatus))', 'const nextStatus = String(req.body.status || "") as BookingStatus; if (!allowed.includes(nextStatus))', 1)
p.write_text(s)
