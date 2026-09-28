from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s = p.read_text()
s = s.replace('import { useMemo, useState } from "react";', 'import { useEffect, useMemo, useState } from "react";', 1)
s = s.replace('  const [notice, setNotice] = useState("");', '  const [notice, setNotice] = useState("");\n  const [publishedWorkers, setPublishedWorkers] = useState<any[]>([]);', 1)
s = s.replace('  const activeWorkers = workforce === "Male" ? workers : [...femaleWorkers, ...femaleAdditionalWorkers];', '  useEffect(() => { fetch("/api/workers/public").then((response) => response.ok ? response.json() : []).then((items) => setPublishedWorkers(items)).catch(() => setPublishedWorkers([])); }, []);\n  const publishedForWorkforce = publishedWorkers.filter((worker) => workforce === "Female" ? worker.gender === "Female" : worker.gender !== "Female");\n  const activeWorkers = workforce === "Male" ? [...workers, ...publishedForWorkforce] : [...femaleWorkers, ...femaleAdditionalWorkers, ...publishedForWorkforce];', 1)
old = '<select value={sort} onChange={(event) => setSort(event.target.value)} className="rounded-full border border-[#dce5d9] bg-white px-4 py-2.5 text-sm font-semibold text-[#52675d] outline-none"><option>Recommended</option><option>Top rated</option><option>Lowest price</option></select>'
new = '<select value={activeCategory} onChange={(event) => setActiveCategory(event.target.value)} className="rounded-full border border-[#dce5d9] bg-white px-4 py-2.5 text-sm font-semibold text-[#52675d] outline-none"><option>All services</option>{activeCategories.map((category) => <option key={category.name}>{category.name}</option>)}</select><select value={sort} onChange={(event) => setSort(event.target.value)} className="rounded-full border border-[#dce5d9] bg-white px-4 py-2.5 text-sm font-semibold text-[#52675d] outline-none"><option>Recommended</option><option>Top rated</option><option>Lowest price</option></select>'
if old not in s: raise SystemExit('directory sort select anchor missing')
s = s.replace(old, new, 1)
s = s.replace('{filteredWorkers.length * 168} verified pros ready to help across KP.', '{filteredWorkers.length} verified pros ready to help across KP.', 1)
p.write_text(s)
