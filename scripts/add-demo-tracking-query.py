from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/BookingTrack.tsx')
s=p.read_text()
old='''  useEffect(() => {
    if (!status?._id) return;
    const refresh = async () => {
      const response = await fetch(`/api/bookings/${status._id}`);'''
new='''  useEffect(() => {
    const bookingFromUrl = new URLSearchParams(window.location.search).get("booking");
    if (!status?._id && bookingFromUrl) {
      void fetch(`/api/bookings/${encodeURIComponent(bookingFromUrl)}`).then((response) => response.ok ? response.json() : null).then((booking) => { if (booking?._id) { setStatus(booking); localStorage.setItem("labrkp_pending_booking", JSON.stringify(booking)); } });
      return;
    }
    if (!status?._id) return;
    const refresh = async () => {
      const response = await fetch(`/api/bookings/${status._id}`);'''
if old not in s: raise SystemExit('tracking effect block not found')
s=s.replace(old,new,1)
p.write_text(s)
