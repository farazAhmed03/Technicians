from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s=p.read_text()
# Add request match back before directory section closes, after empty state.
needle='''{filteredWorkers.length === 0 && <div className="mt-7 rounded-[26px] border border-dashed border-[#cfdacb] bg-white py-16 text-center"><p className="font-display text-xl font-semibold text-[#294139]">No matching workers yet</p><p className="mt-2 text-sm text-[#829087]">Try a broader service or search term.</p></div>}'''
addition=needle+'''<div className="mt-8 flex flex-col items-center justify-between gap-4 rounded-[24px] bg-[#eaf3dc] px-6 py-5 sm:flex-row"><div className="flex items-center gap-3"><div className="grid h-10 w-10 place-items-center rounded-2xl bg-[#d6f477] text-[#355d3d]"><Bell size={18} /></div><p className="text-sm text-[#526853]"><strong className="text-[#294139]">Need something specific?</strong> Tell us what you need and we’ll match you.</p></div><button onClick={() => showNotice("Tell us what you need — matching is coming next.")} className="flex items-center gap-2 rounded-full bg-[#294139] px-5 py-2.5 text-sm font-semibold text-white">Request a match <ArrowRight size={15} /></button></div>'''
if needle not in s: raise SystemExit('directory empty state not found')
s=s.replace(needle,addition,1)
# Replace footer CTA content with worker-only CTA.
start=s.find('      <div className="mx-auto max-w-[1240px] px-5 pb-10')
end=s.find('      <footer className=',start)
if start < 0 or end < 0: raise SystemExit('footer CTA block not found')
worker='''      <div className="mx-auto max-w-[1240px] px-5 pb-10 lg:px-8"><div className="flex flex-col items-center justify-between gap-4 rounded-[24px] bg-[#eaf3dc] px-6 py-6 text-center sm:flex-row sm:text-left"><div><p className="text-xs font-bold uppercase tracking-[0.16em] text-[#789159]">Grow with LABRKP</p><p className="mt-1 text-sm text-[#526853]"><strong className="text-[#294139]">Want to offer your skills?</strong> Join our verified workforce.</p></div><Link href="/become-a-worker" className="flex items-center gap-2 rounded-full bg-[#294139] px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-[#355d4d]">Join us as a worker <ArrowRight size={15} /></Link></div></div>\n'''
s=s[:start]+worker+s[end:]
p.write_text(s)
