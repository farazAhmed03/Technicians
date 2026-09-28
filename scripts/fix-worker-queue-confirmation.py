from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/WorkerSignup.tsx')
s=p.read_text()
old='''    try { const response = await fetch("/api/workers/apply", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(form) }); if (!response.ok) throw new Error("Application could not be submitted"); setSubmitted(true); } catch { setError("Application saved for review. Connect MongoDB to persist it online."); setSubmitted(true); }'''
new='''    try { const response = await fetch("/api/workers/apply", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(form) }); const result = await response.json().catch(() => ({})); if (!response.ok) throw new Error(result.error || "Application could not be submitted"); setSubmitted(true); } catch (submissionError) { setError(submissionError instanceof Error ? submissionError.message : "Application could not be submitted. Please try again."); }'''
if old not in s: raise SystemExit('submit block not found')
s=s.replace(old,new,1)
s=s.replace('''Your application is now <strong>Under Review</strong>. It is not visible in the public directory yet. Only an authorized LABRKP administrator can approve or reject it after checking your documents.''','''Your application is now <strong>Under Review</strong>. It is visible in the administrator’s <strong>Worker Verification</strong> queue for approval. It is not visible in the public directory yet; only an authorized LABRKP administrator can approve or reject it after checking your documents.''',1)
p.write_text(s)
