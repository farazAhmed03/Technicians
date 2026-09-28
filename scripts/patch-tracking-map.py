from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/client/src/pages/BookingTrack.tsx')
s = p.read_text()
old = '<div className="mt-5 flex items-center gap-2 text-sm text-white/70"><MapPin size={16} className="text-[#d8f479]" />{accepted ? `Approximately ${status.eta || "20 minutes"} away from you` : "Worker acceptance is required before live tracking starts"}</div></div>'
new = '<div className="mt-5 flex items-center gap-2 text-sm text-white/70"><MapPin size={16} className="text-[#d8f479]" />{accepted ? `Approximately ${status.etaMinutes || status.eta || "20 minutes"} away from you` : "Worker acceptance is required before live tracking starts"}</div>{accepted && <MapView className="mt-5 h-[240px] overflow-hidden rounded-2xl" initialCenter={status.workerLocation || { lat: 30.6708, lng: 72.9944 }} initialZoom={14} onMapReady={(map) => { if (status.workerLocation) new google.maps.Marker({ map, position: status.workerLocation, title: status.workerName || status.worker }); }} />}</div>'
if old not in s: raise SystemExit('map anchor not found')
s = s.replace(old, new, 1)
s = s.replace('{status.worker.split(" ").map((item: string) => item[0]).join("")}', '{(status.workerName || status.worker).split(" ").map((item: string) => item[0]).join("")}')
s = s.replace('{status.worker}</p>', '{status.workerName || status.worker}</p>')
s = s.replace('{status.customer}</span>', '{status.customer?.fullName || status.customer}</span>')
p.write_text(s)
