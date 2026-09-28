from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/WorkerConsole.tsx')
s=p.read_text()
old='''  const [pendingRequest, setPendingRequest] = useState<any>(() => {
    try { return JSON.parse(localStorage.getItem("labrkp_pending_booking") || "null"); } catch { return null; }
  });
  const [requestStatus, setRequestStatus] = useState(pendingRequest?.status || "Pending");'''
new='''  const workerId = "1";
  const [pendingRequest, setPendingRequest] = useState<any>(null);
  const [requestStatus, setRequestStatus] = useState("Pending");
  const [requestLoading, setRequestLoading] = useState(true);
  useEffect(() => { let active = true; fetch(`/api/workers/${workerId}/bookings`).then((response) => response.ok ? response.json() : []).then((rows) => { if (!active) return; const booking = rows.find((item: any) => ["Pending", "Accepted", "OnTheWay"].includes(item.status)); if (booking) { setPendingRequest(booking); setRequestStatus(booking.status); } else { try { const fallback = JSON.parse(localStorage.getItem("labrkp_pending_booking") || "null"); if (fallback?.workerId === workerId) { setPendingRequest(fallback); setRequestStatus(fallback.status || "Pending"); } } catch {} } }).catch(() => {}).finally(() => { if (active) setRequestLoading(false); }); return () => { active = false; }; }, []);'''
if old not in s: raise SystemExit('state block missing')
s=s.replace(old,new,1)
s=s.replace('const acceptRequest = async () => { setRequestStatus("Accepted"); if (pendingRequest?._id) await fetch(`/api/bookings/${pendingRequest._id}/accept`, { method: "POST" }); if (pendingRequest) localStorage.setItem("labrkp_pending_booking", JSON.stringify({ ...pendingRequest, status: "Accepted", eta: "20 minutes" })); };', 'const acceptRequest = async () => { if (!pendingRequest?._id) return; const response = await fetch(`/api/bookings/${pendingRequest._id}/accept`, { method: "POST" }); if (response.ok) { const updated = await response.json(); setPendingRequest(updated); setRequestStatus(updated.status); localStorage.setItem("labrkp_pending_booking", JSON.stringify(updated)); } };',1)
s=s.replace('{pendingRequest && <section', '{requestLoading && <section className="mt-8 rounded-[26px] border border-[#e4ebe0] bg-white p-6 text-sm text-[#819087]">Checking your booking requests…</section>}{pendingRequest && <section',1)
p.write_text(s)
