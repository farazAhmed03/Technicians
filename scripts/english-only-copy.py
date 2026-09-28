from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s=p.read_text().replace('Worker acceptance ke baad Easypaisa/JazzCash payment process continue hoga.', 'After the worker accepts, the Easypaisa/JazzCash payment process will continue.')
p.write_text(s)
