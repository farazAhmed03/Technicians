from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s=p.read_text()
s=s.replace('''  const [complaintSent, setComplaintSent] = useState(false);''','''  const [complaintSent, setComplaintSent] = useState(false);
  const [complaintId, setComplaintId] = useState("");
  const [appealDetails, setAppealDetails] = useState("");
  const [appealSent, setAppealSent] = useState(false);''',1)
s=s.replace('''setComplaintName(""); setComplaintContact(""); setComplaintDetails(""); setComplaintSent(true); };
''','''setComplaintName(""); setComplaintContact(""); setComplaintDetails(""); setComplaintId(data.complaintId || ""); setComplaintSent(true); };
  const submitAppeal = async () => { if (!complaintId || !appealDetails.trim()) return; const response = await fetch(`/api/complaints/${encodeURIComponent(complaintId)}/appeals`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ customerName: complaintName, details: appealDetails }) }); if (response.ok) { setAppealDetails(""); setAppealSent(true); } };
''',1)
s=s.replace('''{complaintSent && <p className="mt-2 text-xs font-semibold text-[#52733e]">Complaint submitted privately for admin review.</p>}<button onClick={() => void submitComplaint()}''','''{complaintSent && <div className="mt-2 rounded-xl bg-[#edf5e5] p-3 text-xs font-semibold text-[#52733e]">Complaint received. Reference: <span className="font-mono">{complaintId}</span><p className="mt-1 font-normal">If the complaint is resolved and you disagree, you can submit an appeal below.</p><textarea value={appealDetails} onChange={(event) => setAppealDetails(event.target.value)} rows={2} placeholder="Appeal details" className="mt-2 w-full rounded-xl border border-[#d7e5d1] bg-white px-3 py-2 text-xs font-normal" /><button onClick={() => void submitAppeal()} className="mt-2 rounded-full border border-[#8db379] px-3 py-1.5 text-[11px] font-bold">Submit appeal</button>{appealSent && <span className="ml-2 font-normal">Appeal received.</span>}</div>}<button onClick={() => void submitComplaint()}''',1)
p.write_text(s)

p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/AdminVerification.tsx')
s=p.read_text()
s=s.replace('''<button onClick={() => void updateComplaint(complaint, "Investigating")} className="rounded-full border border-[#dce5d9] px-3 py-2 text-xs font-bold text-[#52675b]">Investigate</button>''','''<select value={complaint.priority || "Medium"} onChange={(event) => void updateComplaint(complaint, complaint.status, event.target.value)} className="rounded-full border border-[#dce5d9] bg-white px-3 py-2 text-xs font-bold text-[#52675b]"><option>Low</option><option>Medium</option><option>High</option><option>Urgent</option></select><button onClick={() => void updateComplaint(complaint, "Investigating")} className="rounded-full border border-[#dce5d9] px-3 py-2 text-xs font-bold text-[#52675b]">Investigate</button>''',1)
s=s.replace('''const updateComplaint = async (complaint: any, status: string) => { const response = await fetch(`/api/admin/complaints/${complaint.complaintId}`, { method: "PATCH", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ status }) });''','''const updateComplaint = async (complaint: any, status: string, priority?: string) => { const response = await fetch(`/api/admin/complaints/${complaint.complaintId}`, { method: "PATCH", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ status, priority: priority || complaint.priority }) });''',1)
s=s.replace('''<span className="rounded-full bg-[#fff0c5] px-2.5 py-1 text-[10px] font-bold text-[#96722d]">{complaint.status}</span>''','''<span className="rounded-full bg-[#fff0c5] px-2.5 py-1 text-[10px] font-bold text-[#96722d]">{complaint.status}</span><span className="rounded-full bg-[#ffe8e0] px-2.5 py-1 text-[10px] font-bold text-[#a45843]">Priority: {complaint.priority || "Medium"}</span>''',1)
p.write_text(s)
