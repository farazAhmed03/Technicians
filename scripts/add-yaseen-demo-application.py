from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/server/marketplaceApi.ts')
s=p.read_text()
s=s.replace('"Mansehra"]).has(city)', '"Mansehra", "Kurram"]).has(city)', 1)
needle='const memoryProfiles: any[] = [];'
replacement='''const memoryProfiles: any[] = [];
const demoApplication = { applicationId: "DEMO-MUHAMMAD-YASEEN", ownerOpenId: undefined, name: "Muhammad Yaseen", phone: "03201919360", email: "yaseenn2917@gmail.com", gender: "Male", city: "Kurram", skill: "Developer", experience: "3 years", bio: "Doing my best", documents: { profilePhoto: { key: "demo-profile", url: "https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=512&q=80", fileName: "demo-profile-photo.jpg", contentType: "image/jpeg" }, diplomaProof: { key: "demo-diploma", url: "https://dummyimage.com/1200x900/e8f0e2/203a34.png&text=DEMO+DIPLOMA+PROOF", fileName: "demo-diploma-proof.png", contentType: "image/png" } }, status: "Under Review", reviewNote: "Demo application for testing the administrator approval flow.", createdAt: now(), updatedAt: now() };
if (!memoryApplications.some((item) => item.applicationId === demoApplication.applicationId)) memoryApplications.push(demoApplication);'''
if needle not in s: raise SystemExit('memory profile needle missing')
s=s.replace(needle,replacement,1)
p.write_text(s)

p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/WorkerSignup.tsx')
s=p.read_text().replace('"Mansehra"]', '"Mansehra", "Kurram"]', 1)
p.write_text(s)
