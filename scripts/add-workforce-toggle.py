from pathlib import Path

path = Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
text = path.read_text()
needle = '<h1 className="max-w-[610px]'
toggle = '<div className="mb-5 inline-flex rounded-full border border-white/15 bg-white/[0.07] p-1"><button onClick={() => { setWorkforce("Male"); setActiveCategory("All services"); }} className={`rounded-full px-4 py-2 text-xs font-bold transition ${workforce === "Male" ? "bg-[#d8f479] text-[#263d32]" : "text-white/60 hover:text-white"}`}>Male Workforce</button><button onClick={() => { setWorkforce("Female"); setActiveCategory("All services"); }} className={`rounded-full px-4 py-2 text-xs font-bold transition ${workforce === "Female" ? "bg-[#d8f479] text-[#263d32]" : "text-white/60 hover:text-white"}`}>Female Workforce</button></div>'
if needle not in text:
    raise SystemExit('hero badge not found')
text = text.replace(needle, toggle + needle, 1)
text = text.replace('> Live directory</div><h2', '>{workforce} workforce directory</div><h2', 1)
path.write_text(text)
text = text.replace('Book verified local professionals for the work that keeps your world moving — from a quick fix to a full solar setup.', 'Book verified {workforce.toLowerCase()} professionals for the work that keeps your world moving — from a quick fix to a full solar setup.')
