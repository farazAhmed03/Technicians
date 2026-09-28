from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/AdminVerification.tsx')
s=p.read_text()
needle='<div className="flex items-center gap-4"><button onClick={() => void logout()}'
replacement='<div className="flex items-center gap-4"><Link href="/admin/bookings" className="text-sm font-semibold text-[#52675b]">Booking monitor</Link><button onClick={() => void logout()}'
if needle not in s: raise SystemExit('header needle missing')
p.write_text(s.replace(needle,replacement,1))
