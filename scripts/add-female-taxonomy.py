from pathlib import Path
p = Path('/home/ubuntu/labrkp-workforce/client/src/pages/Home.tsx')
s = p.read_text()
anchor = 'const workers = ['
insert = '''const femaleCategories = [
  { name: "Cleaning Team", count: "Home & deep cleaning", icon: "✦", tint: "bg-[#f8e5ef]", services: ["Home Cleaning", "Deep Cleaning", "Carpet Washing", "Sofa & Mattress Cleaning", "Kitchen & Bathroom Cleaning", "Curtain & Window Cleaning"] },
  { name: "Beauty & Salon", count: "Home salon services", icon: "✿", tint: "bg-[#ffe5ef]", services: ["Home Salon", "Makeup", "Bridal Makeup", "Hair Styling", "Facial", "Manicure & Pedicure", "Waxing & Threading", "Mehndi / Henna", "Bridal Mehndi"] },
  { name: "Laundry Team", count: "Wash, iron & care", icon: "◌", tint: "bg-[#e5f0ff]", services: ["Clothes Washing", "Ironing", "Dry Cleaning", "Bedsheet & Blanket Washing", "Curtain Washing", "Folding & Packing"] },
  { name: "Cooking & Catering", count: "Meals & events", icon: "♨", tint: "bg-[#fff0d8]", services: ["Home Cooking", "Daily Meal Preparation", "Event / Dawat Cooking", "Baking", "Cakes & Desserts", "Homemade / Frozen Food"] },
  { name: "Family Care", count: "Trusted home care", icon: "♡", tint: "bg-[#e4f5e2]", services: ["Babysitting", "Child Care", "Elderly Care", "Female Patient Care", "Home Assistance"] },
  { name: "Female Tutors", count: "Home & online learning", icon: "▣", tint: "bg-[#e9e4ff]", services: ["School Subjects", "Home Tuition", "Online Tuition", "Homework Support", "Exam Preparation", "Basic / Quran Education"] },
  { name: "Tailoring & Handicraft", count: "Stitching & craft", icon: "⌁", tint: "bg-[#f9e8d6]", services: ["Dress Stitching", "Alteration", "Embroidery", "Crochet", "Knitting", "Handicrafts"] },
  { name: "Event & Decoration", count: "Celebrations at home", icon: "✧", tint: "bg-[#e3eff0]", services: ["Home Decoration", "Birthday Decoration", "Bridal Shower", "Event Setup", "Gift Packing"] },
];

'''
if anchor not in s: raise SystemExit('worker anchor missing')
s = s.replace(anchor, insert + anchor, 1)
s = s.replace('const activeWorkers = workforce === "Male" ? workers : femaleWorkers;\n', 'const activeWorkers = workforce === "Male" ? workers : femaleWorkers;\n  const activeCategories = workforce === "Male" ? categories : femaleCategories;\n', 1)
s = s.replace('categories.map((category)', 'activeCategories.map((category)', 1)
s = s.replace('className="mt-7 grid gap-5 lg:grid-cols-3"', 'className="mt-7 grid grid-cols-2 gap-3 md:grid-cols-3 xl:grid-cols-4"', 1)
s = s.replace('relative h-36 overflow-hidden', 'relative h-28 overflow-hidden', 1)
s = s.replace('<div className="p-4">', '<div className="p-3">', 1)
s = s.replace('font-display text-[18px] font-semibold', 'font-display text-[16px] font-semibold', 1)
s = s.replace('font-display text-lg font-semibold', 'font-display text-base font-semibold', 1)
s = s.replace('mt-3 flex flex-wrap gap-1.5', 'mt-2 flex flex-wrap gap-1', 1)
s = s.replace('mt-4 flex items-center gap-1.5', 'mt-2 flex items-center gap-1', 1)
s = s.replace('mt-4 flex items-center gap-2 border-t', 'mt-3 flex items-center gap-1.5 border-t', 1)
p.write_text(s)
