from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s = p.read_text().replace('{"services" in category && <p className="mt-2 line-clamp-2 text-[10px] leading-4 text-[#9aa79d]">{category.services.slice(0, 2).join(" · ")}</p>}', '{"services" in category && Array.isArray(category.services) && <p className="mt-2 line-clamp-2 text-[10px] leading-4 text-[#9aa79d]">{category.services.slice(0, 2).join(" · ")}</p>}')
p.write_text(s)
