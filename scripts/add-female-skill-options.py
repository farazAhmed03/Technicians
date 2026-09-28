from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/WorkerSignup.tsx')
s=p.read_text()
s=s.replace('''const skills = ["Electrical", "Plumbing", "Solar & Energy", "AC & Appliances", "Carpentry", "Cleaning", "Tailoring", "Tech & Electronics", "Other"];''','''const maleSkills = ["Electrical", "Plumbing", "Solar & Energy", "AC & Appliances", "Carpentry", "Tech & Electronics"];
const femaleSkills = ["Home Cleaning", "Deep Cleaning", "Home Salon", "Makeup", "Bridal Makeup", "Hair Styling", "Facial", "Manicure & Pedicure", "Waxing & Threading", "Mehndi / Henna", "Laundry & Ironing", "Home Cooking", "Baking", "Babysitting", "Elderly Care", "Female Patient Care", "Home Tuition", "Quran Education", "Dress Stitching", "Alteration", "Embroidery", "Home Decoration", "Gift Packing"];
const skillsForGender = (gender: string) => [...(gender === "Female" ? femaleSkills : maleSkills), "Other"];''',1)
s=s.replace('''const [form, setForm] = useState({ name: "", phone: "", email: "", gender: "Male", city: "Peshawar", skill: "Electrical",''','''const [form, setForm] = useState({ name: "", phone: "", email: "", gender: "Male", city: "Peshawar", skill: "Electrical",''',1)
old='''<select value={form.gender} onChange={(e) => update("gender", e.target.value)} className="w-full rounded-2xl border border-[#dbe4d9] bg-white px-4 py-3.5 text-sm outline-none"><option>Male</option><option>Female</option></select>'''
new='''<select value={form.gender} onChange={(e) => { const gender = e.target.value; update("gender", gender); update("skill", skillsForGender(gender)[0]); update("customSkill", ""); }} className="w-full rounded-2xl border border-[#dbe4d9] bg-white px-4 py-3.5 text-sm outline-none"><option>Male</option><option>Female</option></select>'''
if old not in s: raise SystemExit('gender select not found')
s=s.replace(old,new,1)
old2='''<select value={form.skill} onChange={(e) => update("skill", e.target.value)} className="w-full rounded-2xl border border-[#dbe4d9] bg-white px-4 py-3.5 text-sm outline-none">{skills.map((skill) => <option key={skill}>{skill}</option>)}</select>'''
new2='''<select value={form.skill} onChange={(e) => update("skill", e.target.value)} className="w-full rounded-2xl border border-[#dbe4d9] bg-white px-4 py-3.5 text-sm outline-none">{skillsForGender(form.gender).map((skill) => <option key={skill}>{skill}</option>)}</select>'''
if old2 not in s: raise SystemExit('skill select not found')
s=s.replace(old2,new2,1)
s=s.replace('''<input value={form.customSkill} onChange={(e) => update("customSkill", e.target.value)} placeholder="e.g. Mobile repair, security, delivery..." className="w-full rounded-2xl border border-[#dbe4d9] px-4 py-3.5 text-sm outline-none focus:border-[#8aab62]" />''','''<input value={form.customSkill} onChange={(e) => update("customSkill", e.target.value)} required={form.skill === "Other"} placeholder={form.skill === "Other" ? "Enter your skill or service *" : "Optional: add another service"} className="w-full rounded-2xl border border-[#dbe4d9] px-4 py-3.5 text-sm outline-none focus:border-[#8aab62]" />''',1)
s=s.replace('''<span className="mb-2 block text-xs font-bold uppercase tracking-[0.13em] text-[#798780]">Primary skill *</span>''','''<span className="mb-2 block text-xs font-bold uppercase tracking-[0.13em] text-[#798780]">Primary skill or service *</span>''',1)
s=s.replace('''Share your skills, city, and experience. Once verified, customers can book you directly.''','''Share your skills, city, and experience. Choose a listed service or select Other to enter any skill not shown. Once verified, customers can book you directly.''',1)
p.write_text(s)
