from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/client/src/pages/AdminVerification.tsx')
s = p.read_text()
s = s.replace('const [status, setStatus] = useState("Under Review");', 'const [status, setStatus] = useState("Under Review");\n  const [loading, setLoading] = useState(false);')
s = s.replace('const load = async () => { const response = await fetch("/api/admin/worker-applications"); if (response.ok) setApplications(await response.json()); };', 'const load = async () => { setLoading(true); const response = await fetch("/api/admin/worker-applications"); if (response.ok) setApplications(await response.json()); setLoading(false); };')
old = '<p className="mt-2 text-sm text-[#718078]">Review new KP worker applications before publishing profiles.</p></div><div className="flex gap-2">'
new = '<p className="mt-2 text-sm text-[#718078]">Review new KP worker applications before publishing profiles.</p><p className="mt-2 text-xs font-semibold text-[#8a9b8f]">Open this page at <span className="rounded bg-white px-2 py-1 text-[#52675b]">/admin/verification</span>, check proof links, then choose Approve or Reject.</p></div><div className="flex flex-wrap gap-2"><button onClick={() => void load()} className="rounded-full border border-[#dce5d9] bg-white px-3 py-2 text-xs font-bold text-[#52675b]">{loading ? "Refreshing…" : "Refresh queue"}</button>'
if old not in s: raise SystemExit('admin header anchor missing')
p.write_text(s.replace(old, new, 1))
