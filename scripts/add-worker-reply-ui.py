from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s=p.read_text()
s=s.replace('  const [reviewSent, setReviewSent] = useState(false);\n  const workerId', '  const [reviewSent, setReviewSent] = useState(false);\n  const [replyDrafts, setReplyDrafts] = useState<Record<string, string>>({});\n  const [replyError, setReplyError] = useState("");\n  const workerId', 1)
needle='''  const submitReview = async () => {'''
reply='''  const submitReply = async (reviewId: string) => { const reply = (replyDrafts[reviewId] || "").trim(); if (!reply) { setReplyError("Reply text is required."); return; } const response = await fetch(`/api/workers/${encodeURIComponent(workerId)}/reviews/${encodeURIComponent(reviewId)}/reply`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ reply }) }); const data = await response.json(); if (!response.ok) { setReplyError(data.error || "Worker login required to reply."); return; } setReviews((current) => current.map((item) => item.reviewId === reviewId ? data : item)); setReplyDrafts((current) => ({ ...current, [reviewId]: "" })); setReplyError(""); };
'''+needle
if needle not in s: raise SystemExit('submit review anchor missing')
s=s.replace(needle,reply,1)
old='<p className="mt-2 text-sm leading-6 text-[#718078]">{review.comment}</p></div>)'
new='''<p className="mt-2 text-sm leading-6 text-[#718078]">{review.comment}</p>{review.reply && <div className="mt-3 rounded-xl bg-[#edf5e5] p-3"><p className="text-[10px] font-bold uppercase tracking-[0.12em] text-[#62805f]">Worker reply</p><p className="mt-1 text-sm leading-5 text-[#496052]">{review.reply}</p></div>}<div className="mt-3"><input value={replyDrafts[review.reviewId] || ""} onChange={(event) => setReplyDrafts((current) => ({ ...current, [review.reviewId]: event.target.value }))} placeholder="Worker reply (sign in as worker)" className="w-full rounded-xl border border-[#d7e5d1] bg-[#f8faf6] px-3 py-2 text-xs outline-none focus:border-[#8aab62]" /><button onClick={() => void submitReply(review.reviewId)} className="mt-2 rounded-full border border-[#cbdcc4] px-3 py-1.5 text-[11px] font-bold text-[#52733e]">Reply as worker</button></div></div>)'''
if old not in s: raise SystemExit('review card anchor missing')
s=s.replace(old,new,1)
s=s.replace('{reviewError && <p className="mt-2 text-xs font-semibold text-[#a45843]">{reviewError}</p>}', '{reviewError && <p className="mt-2 text-xs font-semibold text-[#a45843]">{reviewError}</p>}\n{replyError && <p className="mt-2 text-xs font-semibold text-[#a45843]">{replyError}</p>}',1)
p.write_text(s)
