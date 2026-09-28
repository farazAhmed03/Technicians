from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s = p.read_text()
s = s.replace('<Link href="/console">Worker console</Link>', '<Link href="/become-a-worker">Become a worker</Link><Link href="/console">Worker console</Link>', 1)
p.write_text(s)
