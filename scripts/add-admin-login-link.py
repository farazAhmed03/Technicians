from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s=p.read_text()
needle='<Link href="/console" className="rounded-full bg-[#203a34] px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-[#37564c]">Worker console</Link>'
replacement='<Link href="/admin/verification" className="rounded-full px-3 py-2.5 text-xs font-bold text-[#65736e] transition hover:bg-white hover:text-[#203a34]">Admin login</Link>'+needle
if needle not in s: raise SystemExit('desktop worker console link missing')
s=s.replace(needle,replacement,1)
needle2='<Link href="/console">Worker console</Link>'
replacement2='<Link href="/admin/verification">Admin login</Link>'+needle2
if needle2 not in s: raise SystemExit('mobile worker console link missing')
s=s.replace(needle2,replacement2,1)
p.write_text(s)
