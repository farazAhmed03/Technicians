from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/client/src/pages/WorkerConsole.tsx')
s = p.read_text()
s = s.replace('{pendingRequest.customer} requested {pendingRequest.service}', '{pendingRequest.customer?.fullName || pendingRequest.customer} requested {pendingRequest.service}')
s = s.replace('{requestStatus === "Accepted" && <span className="rounded-full bg-[#d7f477] px-3 py-2 text-[#355d3d]">On the way · ETA 20 min</span>}', '{requestStatus === "Accepted" && <><span className="rounded-full bg-[#d7f477] px-3 py-2 text-[#355d3d]">On the way · ETA 20 min</span><button onClick={startLocationSharing} className="rounded-full bg-[#203a34] px-3 py-2 text-white">Share live GPS</button><span className="rounded-full bg-white px-3 py-2">{locationStatus}</span></>}')
p.write_text(s)
