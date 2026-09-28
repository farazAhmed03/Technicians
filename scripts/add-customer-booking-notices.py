from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/BookingTrack.tsx')
s=p.read_text()
s=s.replace('''  const [status, setStatus] = useState<any>(() => {''','''  const [notifications, setNotifications] = useState<any[]>([]);
  const [status, setStatus] = useState<any>(() => {''',1)
s=s.replace('''const latest = await response.json(); setStatus(latest); localStorage.setItem("labrkp_pending_booking", JSON.stringify(latest)); } };''','''const latest = await response.json(); setStatus(latest); localStorage.setItem("labrkp_pending_booking", JSON.stringify(latest)); const email = latest.customer?.email; if (email) { const noticeResponse = await fetch(`/api/bookings/${latest._id}/notifications?email=${encodeURIComponent(email)}`); if (noticeResponse.ok) setNotifications(await noticeResponse.json()); } };''',1)
s=s.replace('''<div className="mt-8 grid gap-5 lg:grid-cols-[1.1fr_0.9fr]">''','''{notifications.length > 0 && <div className="mt-5 rounded-2xl border border-[#d7e9ad] bg-[#f3fbe5] p-4 text-sm"><p className="font-bold text-[#355d3d]">Latest update</p><p className="mt-1 text-[#65756c]">{notifications[0].message}</p></div>}<div className="mt-8 grid gap-5 lg:grid-cols-[1.1fr_0.9fr]">''',1)
p.write_text(s)
