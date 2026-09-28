from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/WorkerSignup.tsx')
s=p.read_text()
s=s.replace('''    } catch { setError("Application saved for review. Connect MongoDB to persist it online."); setSubmitted(true); }''','''    } catch (submitError) { setError(submitError instanceof Error ? submitError.message : "Application could not be submitted. Please try again."); }''',1)
s=s.replace('''<div className="mt-7 flex justify-center"><Link href="/" className="inline-flex rounded-full bg-[#203a34] px-6 py-3 text-sm font-semibold text-white">Back to marketplace</Link></div>''','''<div className="mt-7 flex flex-wrap justify-center gap-3"><Link href="/worker/application-status" className="inline-flex rounded-full bg-[#203a34] px-6 py-3 text-sm font-semibold text-white">Check application status</Link><Link href="/" className="inline-flex rounded-full border border-[#dce5d9] px-6 py-3 text-sm font-semibold text-[#52675b]">Back to marketplace</Link></div>''',1)
p.write_text(s)
