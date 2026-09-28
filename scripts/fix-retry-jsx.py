from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/AdminVerification.tsx')
s=p.read_text()
s=s.replace('text-[#52733e]`}>{item.channel} resolution', 'text-[#52733e]"}`}>{item.channel} resolution')
p.write_text(s)
