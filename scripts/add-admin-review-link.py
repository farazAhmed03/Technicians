from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/client/src/pages/WorkerSignup.tsx')
s = p.read_text()
old = '<Link href="/" className="mt-7 inline-flex rounded-full bg-[#203a34] px-6 py-3 text-sm font-semibold text-white">Back to marketplace</Link>'
new = '<div className="mt-7 flex flex-wrap justify-center gap-3"><Link href="/" className="inline-flex rounded-full bg-[#203a34] px-6 py-3 text-sm font-semibold text-white">Back to marketplace</Link><Link href="/admin/verification" className="inline-flex rounded-full border border-[#dbe4d9] px-6 py-3 text-sm font-semibold text-[#52675b]">Open admin review queue</Link></div>'
if old not in s: raise SystemExit('success button anchor missing')
p.write_text(s.replace(old, new, 1))
