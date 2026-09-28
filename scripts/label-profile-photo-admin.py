from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/AdminVerification.tsx')
s=p.read_text().replace('key === "diplomaProof" ? "Diploma proof" : "Skill proof"', 'key === "profilePhoto" ? "Profile photo" : key === "diplomaProof" ? "Diploma proof" : "Skill proof"', 1)
p.write_text(s)
