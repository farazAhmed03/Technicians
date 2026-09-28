from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s = p.read_text()
s = s.replace('Start with a category</h2>', '{workforce === "Female" ? "Female services by category" : "Start with a category"}</h2>', 1)
s = s.replace('{filteredWorkers.length * 168} verified pros ready to help across Pakistan.', '{filteredWorkers.length * 168} verified pros ready to help across KP.', 1)
s = s.replace('<Pill tone="green"><ShieldCheck size={13} className="mr-1" />Verified LABRKP worker</Pill><Pill><Star', '<Pill tone="green"><ShieldCheck size={13} className="mr-1" />Verified LABRKP worker</Pill><Pill tone="green"><Check size={13} className="mr-1" />CNIC · Phone · Address checked</Pill><Pill><Star', 1)
p.write_text(s)
