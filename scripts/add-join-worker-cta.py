from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s=p.read_text()
old='''<button onClick={() => showNotice("Tell us what you need — matching is coming next.")} className="flex items-center gap-2 rounded-full bg-[#294139] px-5 py-2.5 text-sm font-semibold text-white">Request a match <ArrowRight size={15} /></button>'''
new='''<div className="flex flex-wrap items-center gap-2"><button onClick={() => showNotice("Tell us what you need — matching is coming next.")} className="flex items-center gap-2 rounded-full bg-[#294139] px-5 py-2.5 text-sm font-semibold text-white">Request a match <ArrowRight size={15} /></button><Link href="/become-a-worker" className="flex items-center gap-2 rounded-full border border-[#b9d391] bg-white px-5 py-2.5 text-sm font-semibold text-[#355d3d] transition hover:bg-[#f4f9ec]">Join us as a worker <ArrowRight size={15} /></Link></div>'''
if old not in s: raise SystemExit('request match button not found')
s=s.replace(old,new,1)
p.write_text(s)
