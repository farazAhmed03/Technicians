from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/BookingTrack.tsx')
s=p.read_text()
start=s.index('  useEffect(() => {')
end=s.index('  const accepted =', start)
block='''  useEffect(() => {\n    if (!status?._id) return;\n    const refresh = async () => {\n      const response = await fetch(`/api/bookings/${status._id}`);\n      if (!response.ok) return;\n      const latest = await response.json();\n      setStatus(latest);\n      localStorage.setItem("labrkp_pending_booking", JSON.stringify(latest));\n      const email = latest.customer?.email;\n      if (email) {\n        const noticeResponse = await fetch(`/api/bookings/${latest._id}/notifications?email=${encodeURIComponent(email)}`);\n        if (noticeResponse.ok) setNotifications(await noticeResponse.json());\n      }\n    };\n    const timer = window.setInterval(refresh, 5000);\n    void refresh();\n    return () => window.clearInterval(timer);\n  }, [status?._id]);\n'''
p.write_text(s[:start]+block+s[end:])
