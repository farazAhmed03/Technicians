from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/AdminVerification.tsx')
s=p.read_text()
s=s.replace('''  const [complaints, setComplaints] = useState<any[]>([]);''','''  const [complaints, setComplaints] = useState<any[]>([]);
  const [appeals, setAppeals] = useState<any[]>([]);''',1)
s=s.replace('''const [queueResponse, workerResponse, reviewResponse, complaintResponse] = await Promise.all([fetch("/api/admin/worker-applications"), fetch("/api/admin/published-workers"), fetch("/api/admin/reviews"), fetch("/api/admin/complaints")]);''','''const [queueResponse, workerResponse, reviewResponse, complaintResponse, appealResponse] = await Promise.all([fetch("/api/admin/worker-applications"), fetch("/api/admin/published-workers"), fetch("/api/admin/reviews"), fetch("/api/admin/complaints"), fetch("/api/admin/complaint-appeals")]);''',1)
s=s.replace('''if (complaintResponse.ok) setComplaints(await complaintResponse.json()); setLoading(false);''','''if (complaintResponse.ok) setComplaints(await complaintResponse.json()); if (appealResponse.ok) setAppeals(await appealResponse.json()); setLoading(false);''',1)
needle='''</section>{previewDoc &&'''
section='''</section><section className="mt-12"><div><p className="text-xs font-bold uppercase tracking-[0.16em] text-[#8a9b8f]">Customer follow-up</p><h2 className="mt-1 font-display text-2xl font-semibold">Complaint appeals</h2></div><div className="mt-4 space-y-3">{appeals.length === 0 && <div className="rounded-[26px] bg-white p-8 text-center text-sm text-[#819087]">No appeals received.</div>}{appeals.map((appeal) => <article key={appeal.appealId} className="rounded-2xl border border-[#e3ebe0] bg-white p-4 shadow-sm"><p className="text-xs font-semibold text-[#8a9991]">Reference: {appeal.complaintId} · {appeal.customerName || "Customer"}</p><p className="mt-2 text-sm leading-6 text-[#65756c]">{appeal.details}</p></article>)}</div></section>{previewDoc &&'''
if needle not in s: raise SystemExit('preview marker not found')
s=s.replace(needle,section,1)
p.write_text(s)
