from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/WorkerConsole.tsx')
s=p.read_text()
s=s.replace('  const [requestLoading, setRequestLoading] = useState(true);', '  const [requestLoading, setRequestLoading] = useState(true);\n  const [accessDenied, setAccessDenied] = useState(false);',1)
s=s.replace('fetch(`/api/workers/${workerId}/bookings`).then((response) => response.ok ? response.json() : [])', 'fetch(`/api/workers/${workerId}/bookings`).then((response) => { if (response.status === 401) { setAccessDenied(true); return []; } return response.ok ? response.json() : []; })',1)
s=s.replace('  if (!user) return <div', '  if (accessDenied) return <div',1)
s=s.replace('<h1 className="mt-5 font-display text-2xl font-semibold text-[#203a34]">Worker login required</h1><p className="mt-3 text-sm leading-6 text-[#718078]">Only an approved LABRKP worker can view assigned customer requests.</p><button onClick={() => startLogin()} className="mt-6 rounded-full bg-[#203a34] px-6 py-3 text-sm font-bold text-white">Sign in</button>', '<h1 className="mt-5 font-display text-2xl font-semibold text-[#203a34]">Approved worker access required</h1><p className="mt-3 text-sm leading-6 text-[#718078]">This account is not linked to an approved worker profile. Sign in with the account used for your approved LABRKP application.</p><button onClick={() => window.location.reload()} className="mt-6 rounded-full bg-[#203a34] px-6 py-3 text-sm font-bold text-white">Check access again</button>',1)
p.write_text(s)
