from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s=p.read_text()
old='''const matchesQuery = !normalized || [worker.name, worker.role, worker.city, ...worker.tags].join(" ").toLowerCase().includes(normalized);
      const matchesCategory = activeCategory === "All services" || worker.role.toLowerCase().includes(activeCategory.toLowerCase()) || worker.tags.some((tag: string) => tag.toLowerCase().includes(activeCategory.toLowerCase()));'''
new='''const workerServices = Array.isArray(worker.services) ? worker.services.map((service: any) => service.name || "") : [];
      const searchable = [worker.name, worker.role, worker.city, ...worker.tags, ...workerServices].join(" ").toLowerCase();
      const matchesQuery = !normalized || searchable.includes(normalized);
      const matchesCategory = activeCategory === "All services" || searchable.includes(activeCategory.toLowerCase());'''
if old not in s: raise SystemExit('filter block not found')
s=s.replace(old,new,1)
old_card='''<div className="mt-7 grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">{activeCategories.map((category) => <button key={category.name} onClick={() => { setActiveCategory(category.name); scrollToDirectory(); }} className="group rounded-[22px] border border-[#e5ebe1] bg-white p-4 text-left transition hover:-translate-y-1 hover:border-[#b7cd9a] hover:shadow-lg"><span className={`grid h-12 w-12 place-items-center rounded-2xl text-2xl ${category.tint}`}>{category.icon}</span><p className="mt-4 text-sm font-bold text-[#294139]">{category.name}</p><p className="mt-1 text-[11px] text-[#8a9891]">{category.count}</p>{"services" in category && Array.isArray(category.services) && <p className="mt-2 line-clamp-2 text-[10px] leading-4 text-[#9aa79d]">{category.services.slice(0, 2).join(" · ")}</p>}</button>)}</div>'''
new_card='''<div className="mt-7 grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-4">{activeCategories.map((category) => <div key={category.name} className="group rounded-[22px] border border-[#e5ebe1] bg-white p-4 text-left transition hover:-translate-y-1 hover:border-[#b7cd9a] hover:shadow-lg"><button onClick={() => { setActiveCategory(category.name); scrollToDirectory(); }} className="w-full text-left"><span className={`grid h-12 w-12 place-items-center rounded-2xl text-2xl ${category.tint}`}>{category.icon}</span><p className="mt-4 text-sm font-bold text-[#294139]">{category.name}</p><p className="mt-1 text-[11px] text-[#8a9891]">{category.count}</p></button>{"services" in category && Array.isArray(category.services) && <div className="mt-3 flex flex-wrap gap-1.5">{category.services.map((service: string) => <button key={service} onClick={() => { setQuery(service); setActiveCategory("All services"); scrollToDirectory(); }} className="rounded-full bg-[#f3f7ed] px-2.5 py-1 text-[10px] font-semibold text-[#587060] transition hover:bg-[#e4f1cc]">{service}</button>)}</div>}</div>)}</div>'''
if old_card not in s: raise SystemExit('category card block not found')
s=s.replace(old_card,new_card,1)
p.write_text(s)
