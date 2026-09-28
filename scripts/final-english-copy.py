from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s=p.read_text().replace('{worker.name} ko aapki booking request bhej di gayi hai. Worker accept karega to aapko status aur ETA updates milengi.', 'Your booking request has been sent to {worker.name}. You will receive status and ETA updates after the worker accepts.')
p.write_text(s)
