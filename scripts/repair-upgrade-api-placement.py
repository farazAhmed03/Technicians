from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/server/marketplaceApi.ts')
s=p.read_text()
start=s.index('  app.get("/api/workers/:id/availability"')
end=s.index('async function bookings()', start)
block=s[start:end]
s=s[:start]+s[end:]
# The final closing brace belongs to registerMarketplaceApi.
pos=s.rfind('\n}')
s=s[:pos]+block+s[pos:]
p.write_text(s)
