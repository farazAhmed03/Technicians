from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s=p.read_text()
s=s.replace('''  const [reviewSent, setReviewSent] = useState(false);''','''  const [reviewSent, setReviewSent] = useState(false);
  const [complaintName, setComplaintName] = useState("");
  const [complaintContact, setComplaintContact] = useState("");
  const [complaintReason, setComplaintReason] = useState("Service quality");
  const [complaintDetails, setComplaintDetails] = useState("");
  const [complaintError, setComplaintError] = useState("");
  const [complaintSent, setComplaintSent] = useState(false);''',1)
marker='''  const submitReview = async () => {'''
fn='''  const submitComplaint = async () => { setComplaintError(""); if (!complaintName.trim() || !complaintDetails.trim()) { setComplaintError("Please enter your name and complaint details."); return; } const response = await fetch(`/api/workers/${encodeURIComponent(workerId)}/complaints`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ workerName: worker.name, customerName: complaintName, customerContact: complaintContact, reason: complaintReason, details: complaintDetails }) }); const data = await response.json(); if (!response.ok) { setComplaintError(data.error || "Unable to submit complaint."); return; } setComplaintName(""); setComplaintContact(""); setComplaintDetails(""); setComplaintSent(true); };
'''
if marker not in s: raise SystemExit('submit review marker not found')
s=s.replace(marker,fn+marker,1)
marker2='''<button onClick={() => void submitReview()} className="mt-3 rounded-full bg-[#203a34] px-4 py-2.5 text-xs font-bold text-white">Submit review</button></div></div></div><aside'''
complaint='''<button onClick={() => void submitReview()} className="mt-3 rounded-full bg-[#203a34] px-4 py-2.5 text-xs font-bold text-white">Submit review</button></div><div className="mt-5 rounded-2xl border border-[#f0d2c8] bg-[#fff8f5] p-4"><p className="text-sm font-semibold text-[#754c42]">Report a concern about this worker</p><p className="mt-1 text-xs leading-5 text-[#9a7166]">Your complaint is private and will be reviewed by LABRKP administration.</p><div className="mt-3 grid gap-3 sm:grid-cols-2"><input value={complaintName} onChange={(event) => setComplaintName(event.target.value)} placeholder="Your name *" className="rounded-xl border border-[#ead8d1] bg-white px-3 py-2.5 text-sm outline-none focus:border-[#c88f7d]" /><input value={complaintContact} onChange={(event) => setComplaintContact(event.target.value)} placeholder="Phone or email (optional)" className="rounded-xl border border-[#ead8d1] bg-white px-3 py-2.5 text-sm outline-none focus:border-[#c88f7d]" /></div><select value={complaintReason} onChange={(event) => setComplaintReason(event.target.value)} className="mt-3 w-full rounded-xl border border-[#ead8d1] bg-white px-3 py-2.5 text-sm outline-none"><option>Service quality</option><option>Unprofessional behavior</option><option>Pricing or payment issue</option><option>Safety concern</option><option>Other</option></select><textarea value={complaintDetails} onChange={(event) => setComplaintDetails(event.target.value)} rows={3} maxLength={2000} placeholder="Describe what happened *" className="mt-3 w-full resize-none rounded-xl border border-[#ead8d1] bg-white px-3 py-2.5 text-sm outline-none focus:border-[#c88f7d]" />{complaintError && <p className="mt-2 text-xs font-semibold text-[#a45843]">{complaintError}</p>}{complaintSent && <p className="mt-2 text-xs font-semibold text-[#52733e]">Complaint submitted privately for admin review.</p>}<button onClick={() => void submitComplaint()} className="mt-3 rounded-full border border-[#d5a393] px-4 py-2.5 text-xs font-bold text-[#a45843]">Submit complaint</button></div></div></div><aside'''
if marker2 not in s: raise SystemExit('review button marker not found')
s=s.replace(marker2,complaint,1)
p.write_text(s)
