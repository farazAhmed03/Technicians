from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s=p.read_text()
hero='''<div className="relative z-10 mt-3 flex flex-col items-center justify-center gap-3 sm:flex-row"><button onClick={() => showNotice("Tell us what you need — matching is coming next.")} className="flex items-center gap-2 rounded-full bg-[#294139] px-5 py-2.5 text-sm font-semibold text-white shadow-sm">Request a match <ArrowRight size={15} /></button><Link href="/become-a-worker" className="flex items-center gap-2 rounded-full border border-[#b9d391] bg-white px-5 py-2.5 text-sm font-semibold text-[#355d3d] shadow-sm transition hover:bg-[#f4f9ec]">Join us as a worker <ArrowRight size={15} /></Link></div>'''
if hero not in s: raise SystemExit('hero CTA not found')
s=s.replace(hero,'',1)
footer='''      <footer className="mx-auto flex max-w-[1240px] flex-col justify-between gap-5 px-5 py-10 text-sm text-[#819087] sm:flex-row sm:items-center lg:px-8">'''
cta='''      <div className="mx-auto max-w-[1240px] px-5 pb-10 lg:px-8"><div className="flex flex-col items-center justify-between gap-4 rounded-[24px] bg-[#eaf3dc] px-6 py-6 text-center sm:flex-row sm:text-left"><div><p className="text-xs font-bold uppercase tracking-[0.16em] text-[#789159]">Grow with LABRKP</p><p className="mt-1 text-sm text-[#526853]"><strong className="text-[#294139]">Need a service or want to offer your skills?</strong> Find the right path below.</p></div><div className="flex flex-wrap items-center justify-center gap-2"><button onClick={() => showNotice("Tell us what you need — matching is coming next.")} className="flex items-center gap-2 rounded-full bg-[#294139] px-5 py-2.5 text-sm font-semibold text-white">Request a match <ArrowRight size={15} /></button><Link href="/become-a-worker" className="flex items-center gap-2 rounded-full border border-[#b9d391] bg-white px-5 py-2.5 text-sm font-semibold text-[#355d3d] transition hover:bg-[#f4f9ec]">Join us as a worker <ArrowRight size={15} /></Link></div></div></div>\n'''+footer
if footer not in s: raise SystemExit('footer not found')
s=s.replace(footer,cta,1)
p.write_text(s)
