from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/AdminVerification.tsx')
s=p.read_text()
s=s.replace('  const [moderatedReviews, setModeratedReviews] = useState<any[]>([]);', '  const [moderatedReviews, setModeratedReviews] = useState<any[]>([]);\n  const [previewDoc, setPreviewDoc] = useState<{ url: string; label: string; type?: string } | null>(null);',1)
old='<a key={key} href={value.url} target="_blank" rel="noreferrer" className="flex items-center gap-1 rounded-full bg-[#e8f0ff] px-3 py-2 text-[#5870a0]">{key === "profilePhoto" ? "Profile photo" : key === "diplomaProof" ? "Diploma proof" : "Skill proof"} <ExternalLink size={12} /></a>'
new='<button key={key} type="button" onClick={() => setPreviewDoc({ url: value.url, label: key === "profilePhoto" ? "Profile photo" : key === "diplomaProof" ? "Diploma proof" : "Skill proof", type: value.contentType })} className="flex items-center gap-1 rounded-full bg-[#e8f0ff] px-3 py-2 text-[#5870a0]">{key === "profilePhoto" ? "Preview photo" : key === "diplomaProof" ? "Preview diploma" : "Preview skill proof"} <ExternalLink size={12} /></button>'
if old not in s: raise SystemExit('document link anchor missing')
s=s.replace(old,new,1)
needle='</section></main></div>;'
modal='''</section>{previewDoc && <div className="fixed inset-0 z-50 grid place-items-center bg-[#10201e]/70 p-5 backdrop-blur-sm"><div className="w-full max-w-2xl rounded-[28px] bg-white p-5 shadow-2xl sm:p-7"><div className="flex items-center justify-between gap-4"><div><p className="text-xs font-bold uppercase tracking-[0.16em] text-[#8a9b8f]">Document preview</p><h2 className="mt-1 font-display text-2xl font-semibold text-[#203a34]">{previewDoc.label}</h2></div><button onClick={() => setPreviewDoc(null)} className="rounded-full bg-[#f0f4ed] px-4 py-2 text-sm font-bold text-[#52675b]">Close</button></div><div className="mt-5 flex max-h-[65vh] min-h-48 items-center justify-center overflow-auto rounded-2xl bg-[#f3f7ed] p-4">{previewDoc.type?.includes("pdf") || previewDoc.url.toLowerCase().includes(".pdf") ? <iframe title={previewDoc.label} src={previewDoc.url} className="h-[60vh] w-full rounded-xl bg-white" /> : <img src={previewDoc.url} alt={previewDoc.label} className="max-h-[60vh] max-w-full rounded-xl object-contain" />}</div><p className="mt-3 text-xs text-[#819087]">Preview only. Opened securely from the uploaded verification document.</p></div></div>}</main></div>;'''
if needle not in s: raise SystemExit('main close anchor missing')
s=s.replace(needle,modal,1)
p.write_text(s)
