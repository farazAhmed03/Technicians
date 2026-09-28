from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s = p.read_text()
old = '<button onClick={() => showNotice("Worker registration opens in the next step.")} className="rounded-full px-4 py-2.5 text-sm font-semibold text-[#50635b] transition hover:bg-white">Become a worker</button>'
new = '<Link href="/become-a-worker" className="rounded-full px-4 py-2.5 text-sm font-semibold text-[#50635b] transition hover:bg-white">Become a worker</Link>'
if old not in s: raise SystemExit('worker signup placeholder not found')
p.write_text(s.replace(old, new, 1))
