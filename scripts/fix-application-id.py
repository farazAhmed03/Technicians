from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/server/marketplaceApi.ts')
s = p.read_text()
s = s.replace('const application = { ...req.body, diplomaProof: undefined, skillProof: undefined, documents, status: "Under Review", createdAt: now(), updatedAt: now() };', 'const application = { applicationId: createReference(), ...req.body, diplomaProof: undefined, skillProof: undefined, documents, status: "Under Review", createdAt: now(), updatedAt: now() };')
s = s.replace('findOneAndUpdate({ _id: req.params.id }, { $set: { status:', 'findOneAndUpdate({ applicationId: req.params.id }, { $set: { status:')
p.write_text(s)
