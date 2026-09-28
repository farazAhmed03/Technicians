from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s = p.read_text().replace('  },,\n  {\n    id: 4,', '  },\n  {\n    id: 4,', 1)
p.write_text(s)
