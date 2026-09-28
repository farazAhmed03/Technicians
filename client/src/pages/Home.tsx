import { useEffect, useMemo, useState } from "react";
import {
  ArrowRight,
  BadgeCheck,
  Bell,
  CalendarDays,
  Check,
  ChevronDown,
  Clock3,
  Compass,
  Filter,
  Heart,
  MapPin,
  Menu,
  MessageCircle,
  Search,
  ShieldCheck,
  SlidersHorizontal,
  Sparkles,
  Star,
  UsersRound,
  X,
  Zap,
} from "lucide-react";
import { Link } from "wouter";

const SOLAR_IMAGE = "https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=1400&q=88";

const categories = [
  { name: "Electrical", count: "842 workers", icon: "⚡", tint: "bg-[#e8f7c8]" },
  { name: "Plumbing", count: "516 workers", icon: "◒", tint: "bg-[#dff0ff]" },
  { name: "AC & Appliances", count: "389 workers", icon: "❄", tint: "bg-[#f1e7ff]" },
  { name: "Carpentry", count: "274 workers", icon: "⌂", tint: "bg-[#ffe5cd]" },
  { name: "Solar & Energy", count: "198 workers", icon: "☼", tint: "bg-[#fff0b8]" },
  { name: "Tech & Electronics", count: "163 workers", icon: "⌁", tint: "bg-[#d9f4e8]" },
];

const femaleCategories = [
  { name: "Cleaning Team", count: "Home & deep cleaning", icon: "✦", tint: "bg-[#f8e5ef]", services: ["Home Cleaning", "Deep Cleaning", "Carpet Washing", "Sofa & Mattress Cleaning", "Kitchen & Bathroom Cleaning", "Curtain & Window Cleaning"] },
  { name: "Beauty & Salon", count: "Home salon services", icon: "✿", tint: "bg-[#ffe5ef]", services: ["Home Salon", "Makeup", "Bridal Makeup", "Hair Styling", "Facial", "Manicure & Pedicure", "Waxing & Threading", "Mehndi / Henna", "Bridal Mehndi"] },
  { name: "Laundry Team", count: "Wash, iron & care", icon: "◌", tint: "bg-[#e5f0ff]", services: ["Clothes Washing", "Ironing", "Dry Cleaning", "Bedsheet & Blanket Washing", "Curtain Washing", "Folding & Packing"] },
  { name: "Cooking & Catering", count: "Meals & events", icon: "♨", tint: "bg-[#fff0d8]", services: ["Home Cooking", "Daily Meal Preparation", "Event / Dawat Cooking", "Baking", "Cakes & Desserts", "Homemade / Frozen Food"] },
  { name: "Family Care", count: "Trusted home care", icon: "♡", tint: "bg-[#e4f5e2]", services: ["Babysitting", "Child Care", "Elderly Care", "Female Patient Care", "Home Assistance"] },
  { name: "Female Tutors", count: "Home & online learning", icon: "▣", tint: "bg-[#e9e4ff]", services: ["School Subjects", "Home Tuition", "Online Tuition", "Homework Support", "Exam Preparation", "Basic / Quran Education"] },
  { name: "Tailoring & Handicraft", count: "Stitching & craft", icon: "⌁", tint: "bg-[#f9e8d6]", services: ["Dress Stitching", "Alteration", "Embroidery", "Crochet", "Knitting", "Handicrafts"] },
  { name: "Event & Decoration", count: "Celebrations at home", icon: "✧", tint: "bg-[#e3eff0]", services: ["Home Decoration", "Birthday Decoration", "Bridal Shower", "Event Setup", "Gift Packing"] },
];

const workers = [
  {
    id: 1,
    name: "Muhammad Usman",
    role: "Electrical & Solar Specialist",
    city: "Kohat, KPK",
    experience: "7 years",
    rating: "4.9",
    reviews: 124,
    jobs: 186,
    price: "1,500",
    image: "https://images.unsplash.com/photo-1621905252507-b35492cc74b4?auto=format&fit=crop&w=900&q=85",
    tags: ["House Wiring", "Solar Installation", "CCTV"],
    availability: "Available today",
    verified: true,
    accent: "#b7df74",
    bio: "A detail-led electrician helping homes and small businesses stay powered, safe and future-ready.",
    services: [
      { name: "House Wiring Inspection", duration: "90 min", price: "Rs. 1,500" },
      { name: "Solar Panel Installation", duration: "4–6 hrs", price: "Rs. 15,000" },
      { name: "CCTV Installation", duration: "3 hrs", price: "Rs. 8,000" },
    ],
  },
  {
    id: 2,
    name: "Ahsan Ullah",
    role: "AC & Appliance Technician",
    city: "Peshawar, KPK",
    experience: "11 years",
    rating: "4.8",
    reviews: 98,
    jobs: 241,
    price: "1,200",
    image: "https://images.unsplash.com/photo-1581094794329-c8112a89af12?auto=format&fit=crop&w=900&q=85",
    tags: ["AC Repair", "Refrigerator", "Maintenance"],
    availability: "Available tomorrow",
    verified: true,
    accent: "#d9e1ff",
    bio: "Fast, clean and transparent appliance care for the moments when your home needs a reliable fix.",
    services: [
      { name: "AC Service & Gas Check", duration: "60 min", price: "Rs. 1,200" },
      { name: "Refrigerator Repair", duration: "2 hrs", price: "Rs. 2,500" },
      { name: "Washing Machine Repair", duration: "90 min", price: "Rs. 1,800" },
    ],
  },
  {
    id: 3,
    name: "Bilal Khan",
    role: "Master Plumber",
    city: "Mardan, KPK",
    experience: "9 years",
    rating: "4.7",
    reviews: 76,
    jobs: 132,
    price: "1,000",
    image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=900&q=85",
    tags: ["Leakage Repair", "Pumps", "Bathroom"],
    availability: "Available today",
    verified: true,
    accent: "#ffe1bd",
    bio: "Precision plumbing, honest estimates and a tidy finish for residential and commercial spaces.",
    services: [
      { name: "Leakage Diagnosis", duration: "45 min", price: "Rs. 1,000" },
      { name: "Water Pump Repair", duration: "2 hrs", price: "Rs. 2,200" },
      { name: "Bathroom Plumbing", duration: "3 hrs", price: "Rs. 3,500" },
    ],
  },
  {
    id: 4,
    name: "Sajid Mehmood",
    role: "Carpentry & Furniture Expert",
    city: "Abbottabad, KPK",
    experience: "12 years",
    rating: "4.9",
    reviews: 112,
    jobs: 208,
    price: "1,800",
    image: "https://images.unsplash.com/photo-1504148455328-c376907d081c?auto=format&fit=crop&w=900&q=85",
    tags: ["Furniture Repair", "Custom Cabinets", "Door Fitting"],
    availability: "Available today",
    verified: true,
    accent: "#f5dfc7",
    bio: "Careful joinery and practical furniture solutions for homes, offices and new spaces.",
    services: [{ name: "Furniture Repair", duration: "2 hrs", price: "Rs. 1,800" }, { name: "Custom Cabinet", duration: "2 days", price: "Rs. 12,000" }, { name: "Door Fitting", duration: "3 hrs", price: "Rs. 2,500" }],
  },
  {
    id: 5,
    name: "Hamza Wali",
    role: "CCTV & Smart Home Technician",
    city: "Nowshera, KPK",
    experience: "8 years",
    rating: "4.8",
    reviews: 83,
    jobs: 177,
    price: "1,400",
    image: "https://images.unsplash.com/photo-1558008258-3256797b43f3?auto=format&fit=crop&w=900&q=85",
    tags: ["CCTV Setup", "Wi-Fi Networks", "Smart Locks"],
    availability: "Available tomorrow",
    verified: true,
    accent: "#dfe8ff",
    bio: "Secure, tidy and easy-to-use technology installations for homes and local businesses.",
    services: [{ name: "CCTV Setup", duration: "3 hrs", price: "Rs. 1,400" }, { name: "Wi-Fi Network Setup", duration: "90 min", price: "Rs. 1,000" }, { name: "Smart Lock Installation", duration: "2 hrs", price: "Rs. 2,200" }],
  },
  {
    id: 6,
    name: "Fahad Khan",
    role: "Solar & Energy Consultant",
    city: "Swat, KPK",
    experience: "10 years",
    rating: "4.9",
    reviews: 91,
    jobs: 164,
    price: "2,000",
    image: "https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=900&q=85",
    tags: ["Solar Survey", "Inverter Repair", "Panel Cleaning"],
    availability: "Available today",
    verified: true,
    accent: "#e7f3c7",
    bio: "Practical solar advice, installation and maintenance that helps families reduce energy costs.",
    services: [{ name: "Solar Site Survey", duration: "90 min", price: "Rs. 2,000" }, { name: "Inverter Repair", duration: "2 hrs", price: "Rs. 2,500" }, { name: "Panel Cleaning", duration: "3 hrs", price: "Rs. 1,500" }],
  },
  {
    id: 7,
    name: "Arif Shah",
    role: "Painting & Home Maintenance Pro",
    city: "Charsadda, KPK",
    experience: "14 years",
    rating: "4.7",
    reviews: 69,
    jobs: 221,
    price: "1,100",
    image: "https://images.unsplash.com/photo-1562259949-e8e7689d7828?auto=format&fit=crop&w=900&q=85",
    tags: ["Interior Paint", "Wall Repair", "Waterproofing"],
    availability: "Available this week",
    verified: true,
    accent: "#ffe5cd",
    bio: "Neat preparation, dependable finishing and honest estimates for home improvement work.",
    services: [{ name: "Room Painting", duration: "1 day", price: "Rs. 1,100" }, { name: "Wall Repair", duration: "3 hrs", price: "Rs. 900" }, { name: "Waterproofing Check", duration: "90 min", price: "Rs. 1,200" }],
  },
  {
    id: 8,
    name: "Naveed Afridi",
    role: "Motorbike & Generator Mechanic",
    city: "Bannu, KPK",
    experience: "9 years",
    rating: "4.8",
    reviews: 57,
    jobs: 148,
    price: "900",
    image: "https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=900&q=85",
    tags: ["Generator Repair", "Bike Service", "Oil Change"],
    availability: "Available today",
    verified: true,
    accent: "#dbeee8",
    bio: "Quick mobile repairs and maintenance for generators, motorbikes and everyday transport.",
    services: [{ name: "Generator Repair", duration: "2 hrs", price: "Rs. 900" }, { name: "Bike Service", duration: "90 min", price: "Rs. 1,000" }, { name: "Oil Change", duration: "30 min", price: "Rs. 500" }],
  }
];

const femaleWorkers = [
  {
    id: 101,
    name: "Ayesha Bibi",
    role: "Home Care & Cleaning Specialist",
    city: "Peshawar, KPK",
    experience: "6 years",
    rating: "4.9",
    reviews: 88,
    jobs: 156,
    price: "1,200",
    image: "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=900&q=85",
    tags: ["Home Cleaning", "Deep Cleaning", "Maintenance"],
    availability: "Available today",
    verified: true,
    accent: "#f3dfef",
    bio: "Thoughtful, dependable home care with a high standard for detail and the comfort of your family.",
    services: [
      { name: "Home Deep Cleaning", duration: "3 hrs", price: "Rs. 1,200" },
      { name: "Kitchen & Bath Cleaning", duration: "2 hrs", price: "Rs. 900" },
      { name: "Move-in Cleaning", duration: "5 hrs", price: "Rs. 3,500" },
    ],
  },
  {
    id: 102,
    name: "Hina Shah",
    role: "Tailoring & Alteration Expert",
    city: "Abbottabad, KPK",
    experience: "8 years",
    rating: "4.8",
    reviews: 64,
    jobs: 119,
    price: "800",
    image: "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=900&q=85",
    tags: ["Alterations", "Bridal Wear", "Custom Stitching"],
    availability: "Available tomorrow",
    verified: true,
    accent: "#f8e7cf",
    bio: "Beautiful, precise stitching and alterations for everyday pieces, celebrations and everything between.",
    services: [
      { name: "Custom Stitching", duration: "3 days", price: "Rs. 2,500" },
      { name: "Dress Alterations", duration: "1 day", price: "Rs. 800" },
      { name: "Bridal Fitting", duration: "90 min", price: "Rs. 1,500" },
    ],
  },
];

const femaleAdditionalWorkers = [
  { id: 103, name: "Sana Noor", role: "Beauty & Salon Specialist", city: "Mardan, KPK", experience: "7 years", rating: "4.9", reviews: 71, jobs: 143, price: "1,500", image: "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=900&q=85", tags: ["Home Salon", "Bridal Makeup", "Mehndi / Henna"], availability: "Available today", verified: true, accent: "#ffe0ea", bio: "Warm, professional beauty services at home for everyday confidence and special celebrations.", services: [{ name: "Home Salon Visit", duration: "2 hrs", price: "Rs. 1,500" }, { name: "Bridal Makeup", duration: "3 hrs", price: "Rs. 8,000" }, { name: "Bridal Mehndi", duration: "3 hrs", price: "Rs. 5,000" }] },
  { id: 104, name: "Nadia Begum", role: "Laundry & Home Care Specialist", city: "Peshawar, KPK", experience: "5 years", rating: "4.8", reviews: 53, jobs: 96, price: "900", image: "https://images.unsplash.com/photo-1582735689369-4fe89db7114c?auto=format&fit=crop&w=900&q=85", tags: ["Clothes Washing", "Ironing", "Curtain Washing"], availability: "Available tomorrow", verified: true, accent: "#e4f0ff", bio: "Reliable laundry care with careful sorting, pressing and convenient home pickup options.", services: [{ name: "Clothes Washing", duration: "1 day", price: "Rs. 900" }, { name: "Ironing", duration: "3 hrs", price: "Rs. 600" }, { name: "Curtain Washing", duration: "2 days", price: "Rs. 1,800" }] },
  { id: 105, name: "Farzana Ali", role: "Cooking & Catering Specialist", city: "Swat, KPK", experience: "9 years", rating: "4.9", reviews: 62, jobs: 118, price: "1,800", image: "https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&w=900&q=85", tags: ["Home Cooking", "Baking", "Frozen Food"], availability: "Available today", verified: true, accent: "#fff0d8", bio: "Homestyle meals, baking and dawat preparation made with care and familiar local flavors.", services: [{ name: "Daily Meal Preparation", duration: "2 hrs", price: "Rs. 1,800" }, { name: "Event / Dawat Cooking", duration: "6 hrs", price: "Rs. 9,000" }, { name: "Cakes & Desserts", duration: "1 day", price: "Rs. 2,500" }] },
  { id: 106, name: "Rabia Khan", role: "Family Care Specialist", city: "Abbottabad, KPK", experience: "8 years", rating: "4.8", reviews: 47, jobs: 89, price: "1,300", image: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=900&q=85", tags: ["Babysitting", "Elderly Care", "Home Assistance"], availability: "Available today", verified: true, accent: "#e4f5e2", bio: "Compassionate, verified family care for children, elders and everyday home assistance.", services: [{ name: "Babysitting", duration: "4 hrs", price: "Rs. 1,300" }, { name: "Elderly Care", duration: "6 hrs", price: "Rs. 2,000" }, { name: "Home Assistance", duration: "3 hrs", price: "Rs. 1,000" }] },
  { id: 107, name: "Maryam Yousaf", role: "Female Tutor", city: "Nowshera, KPK", experience: "6 years", rating: "4.9", reviews: 38, jobs: 74, price: "1,000", image: "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=900&q=85", tags: ["Home Tuition", "Exam Preparation", "Quran Education"], availability: "Available tomorrow", verified: true, accent: "#e9e4ff", bio: "Patient, structured tutoring for school subjects, homework support and Quran education.", services: [{ name: "Home Tuition", duration: "60 min", price: "Rs. 1,000" }, { name: "Exam Preparation", duration: "90 min", price: "Rs. 1,400" }, { name: "Basic / Quran Education", duration: "45 min", price: "Rs. 700" }] },
  { id: 108, name: "Iqra Shah", role: "Event & Decoration Specialist", city: "Kohat, KPK", experience: "5 years", rating: "4.7", reviews: 29, jobs: 56, price: "2,500", image: "https://images.unsplash.com/photo-1519225421980-715cb0215aed?auto=format&fit=crop&w=900&q=85", tags: ["Birthday Decoration", "Bridal Shower", "Gift Packing"], availability: "Available tomorrow", verified: true, accent: "#e3eff0", bio: "Beautiful home celebrations, thoughtful gift packing and polished event setups.", services: [{ name: "Birthday Decoration", duration: "3 hrs", price: "Rs. 2,500" }, { name: "Bridal Shower Setup", duration: "5 hrs", price: "Rs. 6,000" }, { name: "Gift Packing", duration: "90 min", price: "Rs. 800" }] },
];

const workerImages = [
  "https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=700&q=85",
  "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=700&q=85",
  "https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=700&q=85",
];

function Pill({ children, tone = "light" }: { children: React.ReactNode; tone?: "light" | "green" | "dark" }) {
  const toneClasses = {
    light: "bg-[#f2f4ef] text-[#5b6865]",
    green: "bg-[#dff3a9] text-[#223522]",
    dark: "bg-[#1f302e] text-white",
  };
  return <span className={`inline-flex items-center rounded-full px-3 py-1.5 text-[11px] font-semibold tracking-wide ${toneClasses[tone]}`}>{children}</span>;
}

function VerifiedMark() {
  return <span className="inline-flex h-5 w-5 items-center justify-center rounded-full bg-[#ccf477] text-[#1f302e]" title="Verified LABRKP worker"><BadgeCheck size={13} strokeWidth={2.5} /></span>;
}

function WorkerCard({ worker, onOpen }: { worker: (typeof workers)[number]; onOpen: (worker: (typeof workers)[number]) => void }) {
  const [liked, setLiked] = useState(false);
  return (
    <article role="button" tabIndex={0} onClick={() => onOpen(worker)} onKeyDown={(event) => { if (event.key === "Enter" || event.key === " ") onOpen(worker); }} className="group cursor-pointer overflow-hidden rounded-[22px] border border-[#e6ebe2] bg-white shadow-[0_10px_26px_rgba(30,48,40,0.05)] transition duration-200 hover:-translate-y-1 hover:shadow-[0_20px_45px_rgba(30,48,40,0.1)]">
      <div className="relative h-28 overflow-hidden" style={{ backgroundColor: worker.accent }}>
        <img src={worker.image} alt={worker.name} className="h-full w-full object-cover transition duration-500 group-hover:scale-105" />
        <div className="absolute inset-0 bg-gradient-to-t from-[#162524]/55 via-transparent to-transparent" />
        <div className="absolute left-4 top-4 flex items-center gap-2">
          <Pill tone="green"><span className="mr-1 h-1.5 w-1.5 rounded-full bg-[#4e7c2d]" />{worker.availability}</Pill>
        </div>
        <button onClick={(event) => { event.stopPropagation(); setLiked((value) => !value); }} className="absolute right-4 top-4 grid h-9 w-9 place-items-center rounded-full bg-white/90 text-[#263c37] backdrop-blur transition hover:bg-white" aria-label="Save worker">
          <Heart size={16} fill={liked ? "#df765d" : "none"} color={liked ? "#df765d" : "currentColor"} />
        </button>
        <div className="absolute bottom-4 left-4 flex items-center gap-2 text-white">
          <span className="flex items-center gap-1 text-xs font-semibold"><Star size={14} fill="#d6f778" color="#d6f778" />{worker.rating}</span>
          <span className="text-xs text-white/75">({worker.reviews} reviews)</span>
        </div>
      </div>
      <div className="p-3">
        <div className="flex items-start justify-between gap-3">
          <div>
            <div className="flex items-center gap-2"><h3 className="font-display text-[16px] font-semibold text-[#1c2c2a]">{worker.name}</h3><VerifiedMark /></div>
            <p className="mt-1 text-xs text-[#65716e]">{worker.role}</p>
          </div>
          <div className="text-right"><p className="text-[10px] font-bold uppercase tracking-[0.16em] text-[#97a19d]">From</p><p className="mt-0.5 font-display text-base font-semibold text-[#203331]">Rs. {worker.price}</p></div>
        </div>
        <div className="mt-3 flex items-center gap-1.5 text-[11px] text-[#75817d]"><MapPin size={14} />{worker.city}<span className="mx-1 text-[#c5cdc5]">•</span><span>{worker.experience} exp.</span></div>
        <div className="mt-2 flex flex-wrap gap-1">{worker.tags.slice(0, 3).map((tag) => <Pill key={tag}>{tag}</Pill>)}</div>
        <div className="mt-3 flex items-center gap-1.5 border-t border-[#edf0eb] pt-3"><button onClick={(event) => { event.stopPropagation(); onOpen(worker); }} className="flex-1 rounded-full border border-[#d9e2d8] px-3 py-2 text-xs font-semibold text-[#2a413b] transition hover:border-[#9caf8b] hover:bg-[#f5f8f0]">View profile</button><button onClick={(event) => { event.stopPropagation(); onOpen(worker); }} className="flex-1 rounded-full bg-[#243b37] px-3 py-2 text-xs font-semibold text-white transition hover:bg-[#35534a]">Book now</button></div>
      </div>
    </article>
  );
}

function BookingModal({ worker, onClose }: { worker: (typeof workers)[number]; onClose: () => void }) {
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState("");
  const [service, setService] = useState(worker.services[0].name);
  const [form, setForm] = useState({ fullName: "", phone: "", email: "", date: "", time: "", location: "", notes: "", paymentMethod: "Easypaisa", consent: false, liveEta: true });
  const selected = worker.services.find((item) => item.name === service) ?? worker.services[0];
  const price = Number(selected.price.replace(/[^0-9]/g, ""));
  const commission = Math.round(price * 0.03);
  const update = (key: keyof typeof form, value: string | boolean) => setForm((current) => ({ ...current, [key]: value }));
  const submit = async () => {
    if (!form.fullName || !form.phone || !form.email || !form.date || !form.time || !form.location || !form.consent) {
      setError("Please complete all required fields and accept the contact consent.");
      return;
    }
    const request = { workerId: String((worker as any).applicationId || worker.id || worker.name.toLowerCase().replace(/\s+/g, "-")), workerName: worker.name, customer: { fullName: form.fullName, phone: form.phone, email: form.email }, service: selected.name, date: form.date, time: form.time, location: form.location, notes: form.notes, paymentMethod: form.paymentMethod.toLowerCase() === "cash after service" ? "cash" : form.paymentMethod.toLowerCase(), price, consent: form.consent, liveEta: form.liveEta };
    try {
      const response = await fetch("/api/bookings", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(request) });
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || "Unable to create booking");
      localStorage.setItem("labrkp_pending_booking", JSON.stringify(result.booking));
      setSubmitted(true);
    } catch (submitError) {
      localStorage.setItem("labrkp_pending_booking", JSON.stringify({ ...request, _id: `local-${Date.now()}`, id: Date.now(), worker: worker.name, customer: form.fullName, commission, workerEarning: price - commission, status: "Pending" }));
      setError(submitError instanceof Error ? `${submitError.message}. Demo request saved locally.` : "Unable to create booking.");
    }
  };
  if (submitted) return <div className="fixed inset-0 z-50 grid place-items-center bg-[#10201e]/60 p-4 backdrop-blur-sm"><div className="w-full max-w-md rounded-[28px] bg-white p-8 text-center shadow-2xl"><div className="mx-auto grid h-16 w-16 place-items-center rounded-full bg-[#dff3a9] text-[#355b33]"><Check size={30} strokeWidth={2.6} /></div><p className="mt-5 text-xs font-bold uppercase tracking-[0.2em] text-[#7b8e84]">Request sent to worker</p><h2 className="mt-2 font-display text-3xl font-semibold text-[#1c2c2a]">Waiting for acceptance.</h2><p className="mx-auto mt-3 max-w-xs text-sm leading-6 text-[#65716e]">Your booking request has been sent to {worker.name}. You will receive status and ETA updates after the worker accepts.</p><Link href="/track" onClick={onClose} className="mt-7 block w-full rounded-full bg-[#243b37] py-3.5 text-sm font-semibold text-white">View booking status</Link></div></div>;
  return <div className="fixed inset-0 z-50 overflow-y-auto bg-[#10201e]/60 p-4 backdrop-blur-sm"><div className="flex min-h-full items-center justify-center py-8"><div className="w-full max-w-3xl rounded-[30px] bg-[#f8faf6] shadow-2xl"><div className="flex items-start justify-between border-b border-[#e6ebe2] px-6 py-5 sm:px-8"><div><p className="text-xs font-bold uppercase tracking-[0.18em] text-[#8a9993]">Book {worker.name}</p><h2 className="mt-1 font-display text-2xl font-semibold text-[#1c2c2a]">Share your details</h2></div><button onClick={onClose} className="grid h-9 w-9 place-items-center rounded-full bg-white text-[#51605a] shadow-sm"><X size={18} /></button></div><div className="m-5 rounded-2xl bg-[#fff1ea] px-4 py-3 text-sm font-semibold text-[#7d5b4e]">Customer ki details worker ko request ke saath send hongi.</div><div className="grid gap-6 p-6 pt-1 sm:grid-cols-[1fr_0.78fr] sm:p-8 sm:pt-1"><div className="space-y-4"><div className="grid gap-4 sm:grid-cols-2"><label className="block"><span className="mb-2 block text-xs font-bold uppercase tracking-[0.13em] text-[#798780]">Full name *</span><input value={form.fullName} onChange={(e) => update("fullName", e.target.value)} placeholder="Your name" className="w-full rounded-2xl border border-[#dbe4d9] bg-white px-4 py-3.5 text-sm outline-none focus:border-[#8aab62]" /></label><label className="block"><span className="mb-2 block text-xs font-bold uppercase tracking-[0.13em] text-[#798780]">Phone *</span><input value={form.phone} onChange={(e) => update("phone", e.target.value)} placeholder="03XX XXXXXXX" className="w-full rounded-2xl border border-[#dbe4d9] bg-white px-4 py-3.5 text-sm outline-none focus:border-[#8aab62]" /></label></div><label className="block"><span className="mb-2 block text-xs font-bold uppercase tracking-[0.13em] text-[#798780]">Email *</span><input type="email" value={form.email} onChange={(e) => update("email", e.target.value)} placeholder="you@example.com" className="w-full rounded-2xl border border-[#dbe4d9] bg-white px-4 py-3.5 text-sm outline-none focus:border-[#8aab62]" /></label><label className="block"><span className="mb-2 block text-xs font-bold uppercase tracking-[0.13em] text-[#798780]">Select service *</span><select value={service} onChange={(e) => setService(e.target.value)} className="w-full rounded-2xl border border-[#dbe4d9] bg-white px-4 py-3.5 text-sm outline-none focus:border-[#8aab62]">{worker.services.map((item) => <option key={item.name} value={item.name}>{item.name} · {item.price}</option>)}</select></label><div className="grid gap-4 sm:grid-cols-2"><label className="block"><span className="mb-2 block text-xs font-bold uppercase tracking-[0.13em] text-[#798780]">Date *</span><input type="date" value={form.date} onChange={(e) => update("date", e.target.value)} className="w-full rounded-2xl border border-[#dbe4d9] bg-white px-4 py-3.5 text-sm outline-none focus:border-[#8aab62]" /></label><label className="block"><span className="mb-2 block text-xs font-bold uppercase tracking-[0.13em] text-[#798780]">Time *</span><input type="time" value={form.time} onChange={(e) => update("time", e.target.value)} className="w-full rounded-2xl border border-[#dbe4d9] bg-white px-4 py-3.5 text-sm outline-none focus:border-[#8aab62]" /></label></div><label className="block"><span className="mb-2 block text-xs font-bold uppercase tracking-[0.13em] text-[#798780]">Service location *</span><textarea rows={2} value={form.location} onChange={(e) => update("location", e.target.value)} placeholder="House / office address, area and landmark" className="w-full resize-none rounded-2xl border border-[#dbe4d9] bg-white px-4 py-3.5 text-sm outline-none placeholder:text-[#a3afa9] focus:border-[#8aab62]" /></label><label className="block"><span className="mb-2 block text-xs font-bold uppercase tracking-[0.13em] text-[#798780]">Notes (optional)</span><textarea rows={2} value={form.notes} onChange={(e) => update("notes", e.target.value)} placeholder="Special request or extra details..." className="w-full resize-none rounded-2xl border border-[#dbe4d9] bg-white px-4 py-3.5 text-sm outline-none placeholder:text-[#a3afa9] focus:border-[#8aab62]" /></label><label className="block"><span className="mb-2 block text-xs font-bold uppercase tracking-[0.13em] text-[#798780]">Payment method</span><select value={form.paymentMethod} onChange={(e) => update("paymentMethod", e.target.value)} className="w-full rounded-2xl border border-[#dbe4d9] bg-white px-4 py-3.5 text-sm outline-none focus:border-[#8aab62]"><option>Easypaisa</option><option>JazzCash</option><option>Cash after service</option></select><span className="mt-1 block text-[11px] text-[#8c9991]">Online gateway payment will be enabled after merchant credentials are connected.</span></label><label className="flex items-start gap-3 text-sm text-[#4e6258]"><input type="checkbox" checked={form.consent} onChange={(e) => update("consent", e.target.checked)} className="mt-1 h-4 w-4 accent-[#5e824b]" /><span>I agree to be contacted about this booking request. *</span></label>{error && <p className="rounded-xl bg-[#ffe8e0] px-3 py-2 text-xs font-semibold text-[#a45843]">{error}</p>}</div><aside className="h-fit rounded-[24px] bg-[#203532] p-5 text-white"><div className="flex items-center gap-3"><img src={worker.image} alt="" className="h-12 w-12 rounded-2xl object-cover" /><div><p className="font-semibold">{worker.name}</p><p className="mt-0.5 text-xs text-white/60">{worker.city}</p></div><VerifiedMark /></div><div className="my-5 h-px bg-white/10" /><div className="space-y-3 text-sm"><div className="flex justify-between gap-4 text-white/65"><span>Service fee</span><span className="text-white">Rs. {price.toLocaleString()}</span></div><div className="flex justify-between gap-4 text-white/65"><span>Platform commission (3%)</span><span className="text-[#d8f479]">Rs. {commission.toLocaleString()}</span></div><div className="flex justify-between gap-4 border-t border-white/10 pt-3 text-white/65"><span>Worker receives</span><span className="font-semibold text-white">Rs. {(price - commission).toLocaleString()}</span></div></div><label className="mt-6 flex items-start gap-3 rounded-2xl bg-white/10 p-3 text-xs leading-5 text-white/70"><input type="checkbox" checked={form.liveEta} onChange={(e) => update("liveEta", e.target.checked)} className="mt-1 h-4 w-4 accent-[#d8f479]" />Share live ETA updates when the worker accepts and starts travelling</label><button onClick={submit} className="mt-5 flex w-full items-center justify-center gap-2 rounded-full bg-[#d7f477] py-3.5 text-sm font-bold text-[#263b31]">Send booking request <ArrowRight size={16} /></button><p className="mt-3 text-center text-[11px] leading-4 text-white/45">After the worker accepts, the Easypaisa/JazzCash payment process will continue.</p></aside></div></div></div></div>;
}
function WorkerDetail({ worker, onClose, onBook, onRatingUpdated }: { worker: (typeof workers)[number]; onClose: () => void; onBook: () => void; onRatingUpdated: (summary: { rating: string; reviews: number }) => void }) {
  const [reviews, setReviews] = useState<any[]>([]);
  const [customerName, setCustomerName] = useState("");
  const [comment, setComment] = useState("");
  const [rating, setRating] = useState(5);
  const [reviewError, setReviewError] = useState("");
  const [reviewSent, setReviewSent] = useState(false);
  const [complaintName, setComplaintName] = useState("");
  const [complaintContact, setComplaintContact] = useState("");
  const [complaintReason, setComplaintReason] = useState("Service quality");
  const [complaintDetails, setComplaintDetails] = useState("");
  const [complaintError, setComplaintError] = useState("");
  const [complaintSent, setComplaintSent] = useState(false);
  const [complaintId, setComplaintId] = useState("");
  const [appealDetails, setAppealDetails] = useState("");
  const [appealSent, setAppealSent] = useState(false);
  const [replyDrafts, setReplyDrafts] = useState<Record<string, string>>({});
  const [replyError, setReplyError] = useState("");
  const workerId = String((worker as any).applicationId || worker.id);
  useEffect(() => { fetch(`/api/workers/${encodeURIComponent(workerId)}/reviews`).then((response) => response.ok ? response.json() : { reviews: [] }).then((data) => { setReviews(data.reviews || []); if (data.summary) onRatingUpdated(data.summary); }).catch(() => setReviews([])); }, [workerId]);
  const submitReply = async (reviewId: string) => { const reply = (replyDrafts[reviewId] || "").trim(); if (!reply) { setReplyError("Reply text is required."); return; } const response = await fetch(`/api/workers/${encodeURIComponent(workerId)}/reviews/${encodeURIComponent(reviewId)}/reply`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ reply }) }); const data = await response.json(); if (!response.ok) { setReplyError(data.error || "Worker login required to reply."); return; } setReviews((current) => current.map((item) => item.reviewId === reviewId ? data : item)); setReplyDrafts((current) => ({ ...current, [reviewId]: "" })); setReplyError(""); };
  const submitComplaint = async () => { setComplaintError(""); if (!complaintName.trim() || !complaintDetails.trim()) { setComplaintError("Please enter your name and complaint details."); return; } const response = await fetch(`/api/workers/${encodeURIComponent(workerId)}/complaints`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ workerName: worker.name, customerName: complaintName, customerContact: complaintContact, reason: complaintReason, details: complaintDetails }) }); const data = await response.json(); if (!response.ok) { setComplaintError(data.error || "Unable to submit complaint."); return; } setComplaintName(""); setComplaintContact(""); setComplaintDetails(""); setComplaintId(data.complaintId || ""); setComplaintSent(true); };
  const submitAppeal = async () => { if (!complaintId || !appealDetails.trim()) return; const response = await fetch(`/api/complaints/${encodeURIComponent(complaintId)}/appeals`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ customerName: complaintName, details: appealDetails }) }); if (response.ok) { setAppealDetails(""); setAppealSent(true); } };
  const submitReview = async () => {
    setReviewError("");
    if (!customerName.trim() || !comment.trim()) { setReviewError("Please enter your name and review."); return; }
    const response = await fetch(`/api/workers/${encodeURIComponent(workerId)}/reviews`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ customerName, comment, rating }) });
    const data = await response.json();
    if (!response.ok) { setReviewError(data.error || "Unable to submit review."); return; }
    setReviews((current) => [data.review, ...current]); onRatingUpdated(data.summary); setCustomerName(""); setComment(""); setReviewSent(true);
  };
  return <div className="fixed inset-0 z-40 overflow-y-auto bg-[#10201e]/60 p-4 backdrop-blur-sm"><div className="flex min-h-full items-center justify-center py-8"><div className="w-full max-w-4xl overflow-hidden rounded-[30px] bg-[#f8faf6] shadow-2xl"><div className="relative h-56 sm:h-72"><img src={worker.image} alt={worker.name} className="h-full w-full object-cover" /><div className="absolute inset-0 bg-gradient-to-t from-[#162524]/80 to-transparent" /><button onClick={onClose} className="absolute right-5 top-5 grid h-10 w-10 place-items-center rounded-full bg-white/90 text-[#263c37]"><X size={18} /></button><div className="absolute bottom-5 left-6 right-6 flex flex-col justify-between gap-4 text-white sm:flex-row sm:items-end"><div><div className="flex items-center gap-2"><h2 className="font-display text-3xl font-semibold">{worker.name}</h2><VerifiedMark /></div><p className="mt-1 text-sm text-white/75">{worker.role} · {worker.city}</p></div><button onClick={onBook} className="flex items-center justify-center gap-2 rounded-full bg-[#d7f477] px-5 py-3 text-sm font-bold text-[#263b31]">Book this worker <ArrowRight size={16} /></button></div></div><div className="grid gap-8 p-6 sm:grid-cols-[1.1fr_0.9fr] sm:p-8"><div><div className="flex flex-wrap gap-2"><Pill tone="green"><ShieldCheck size={13} className="mr-1" />Verified LABRKP worker</Pill><Pill tone="green"><Check size={13} className="mr-1" />CNIC · Phone · Address checked</Pill><Pill><Star size={13} className="mr-1 fill-[#c18b27] text-[#c18b27]" />{worker.rating} · {worker.reviews} reviews</Pill><Pill><UsersRound size={13} className="mr-1" />{worker.jobs} jobs completed</Pill></div><p className="mt-6 text-sm leading-7 text-[#5f6e68]">{worker.bio} {worker.name} is known for clear communication, punctual arrivals and work that holds up beyond the handover.</p><div className="mt-7"><div className="flex items-center justify-between"><h3 className="font-display text-xl font-semibold text-[#1c2c2a]">Services & pricing</h3><span className="text-xs text-[#8b9992]">Updated this week</span></div><div className="mt-4 space-y-3">{worker.services.map((item) => <div key={item.name} className="flex items-center justify-between gap-4 rounded-2xl border border-[#e4ebe0] bg-white px-4 py-3.5"><div><p className="text-sm font-semibold text-[#2c403a]">{item.name}</p><p className="mt-1 flex items-center gap-1 text-xs text-[#8b9992]"><Clock3 size={12} />{item.duration}</p></div><p className="font-display text-base font-semibold text-[#2b493d]">{item.price}</p></div>)}</div></div><div className="mt-8 border-t border-[#e4ebe0] pt-6"><div className="flex items-center justify-between"><h3 className="font-display text-xl font-semibold text-[#1c2c2a]">Customer reviews</h3><span className="text-xs text-[#8b9992]">{reviews.length} submitted</span></div><div className="mt-4 space-y-3">{reviews.slice(0, 3).map((review) => <div key={review.reviewId} className="rounded-2xl bg-white p-4"><div className="flex items-center justify-between gap-3"><p className="text-sm font-semibold text-[#2c403a]">{review.customerName}</p><span className="flex items-center gap-1 text-xs font-bold text-[#9b7424]"><Star size={12} className="fill-current" />{review.rating}/5</span></div><p className="mt-2 text-sm leading-6 text-[#718078]">{review.comment}</p>{review.reply && <div className="mt-3 rounded-xl bg-[#edf5e5] p-3"><p className="text-[10px] font-bold uppercase tracking-[0.12em] text-[#62805f]">Worker reply</p><p className="mt-1 text-sm leading-5 text-[#496052]">{review.reply}</p></div>}<div className="mt-3"><input value={replyDrafts[review.reviewId] || ""} onChange={(event) => setReplyDrafts((current) => ({ ...current, [review.reviewId]: event.target.value }))} placeholder="Worker reply (sign in as worker)" className="w-full rounded-xl border border-[#d7e5d1] bg-[#f8faf6] px-3 py-2 text-xs outline-none focus:border-[#8aab62]" /><button onClick={() => void submitReply(review.reviewId)} className="mt-2 rounded-full border border-[#cbdcc4] px-3 py-1.5 text-[11px] font-bold text-[#52733e]">Reply as worker</button></div></div>)}{reviews.length === 0 && <p className="rounded-2xl bg-white p-4 text-sm text-[#819087]">No reviews yet — be the first customer to share feedback.</p>}</div><div className="mt-5 rounded-2xl bg-[#edf5e5] p-4"><p className="text-sm font-semibold text-[#314a3c]">Share your experience</p><div className="mt-3 grid gap-3 sm:grid-cols-2"><input value={customerName} onChange={(event) => setCustomerName(event.target.value)} placeholder="Your name" className="rounded-xl border border-[#d7e5d1] bg-white px-3 py-2.5 text-sm outline-none focus:border-[#8aab62]" /><select value={rating} onChange={(event) => setRating(Number(event.target.value))} className="rounded-xl border border-[#d7e5d1] bg-white px-3 py-2.5 text-sm outline-none"><option value={5}>5 stars — Excellent</option><option value={4}>4 stars — Good</option><option value={3}>3 stars — Okay</option><option value={2}>2 stars — Needs improvement</option><option value={1}>1 star — Poor</option></select></div><textarea value={comment} onChange={(event) => setComment(event.target.value)} rows={3} placeholder="Tell future customers about the service..." className="mt-3 w-full resize-none rounded-xl border border-[#d7e5d1] bg-white px-3 py-2.5 text-sm outline-none focus:border-[#8aab62]" />{reviewError && <p className="mt-2 text-xs font-semibold text-[#a45843]">{reviewError}</p>}
{replyError && <p className="mt-2 text-xs font-semibold text-[#a45843]">{replyError}</p>}{reviewSent && <p className="mt-2 text-xs font-semibold text-[#52733e]">Thank you — the worker rating has been updated.</p>}<button onClick={() => void submitReview()} className="mt-3 rounded-full bg-[#203a34] px-4 py-2.5 text-xs font-bold text-white">Submit review</button></div><div className="mt-5 rounded-2xl border border-[#f0d2c8] bg-[#fff8f5] p-4"><p className="text-sm font-semibold text-[#754c42]">Report a concern about this worker</p><p className="mt-1 text-xs leading-5 text-[#9a7166]">Your complaint is private and will be reviewed by LABRKP administration.</p><div className="mt-3 grid gap-3 sm:grid-cols-2"><input value={complaintName} onChange={(event) => setComplaintName(event.target.value)} placeholder="Your name *" className="rounded-xl border border-[#ead8d1] bg-white px-3 py-2.5 text-sm outline-none focus:border-[#c88f7d]" /><input value={complaintContact} onChange={(event) => setComplaintContact(event.target.value)} placeholder="Phone or email (optional)" className="rounded-xl border border-[#ead8d1] bg-white px-3 py-2.5 text-sm outline-none focus:border-[#c88f7d]" /></div><select value={complaintReason} onChange={(event) => setComplaintReason(event.target.value)} className="mt-3 w-full rounded-xl border border-[#ead8d1] bg-white px-3 py-2.5 text-sm outline-none"><option>Service quality</option><option>Unprofessional behavior</option><option>Pricing or payment issue</option><option>Safety concern</option><option>Other</option></select><textarea value={complaintDetails} onChange={(event) => setComplaintDetails(event.target.value)} rows={3} maxLength={2000} placeholder="Describe what happened *" className="mt-3 w-full resize-none rounded-xl border border-[#ead8d1] bg-white px-3 py-2.5 text-sm outline-none focus:border-[#c88f7d]" />{complaintError && <p className="mt-2 text-xs font-semibold text-[#a45843]">{complaintError}</p>}{complaintSent && <div className="mt-2 rounded-xl bg-[#edf5e5] p-3 text-xs font-semibold text-[#52733e]">Complaint received. Reference: <span className="font-mono">{complaintId}</span><p className="mt-1 font-normal">If the complaint is resolved and you disagree, you can submit an appeal below.</p><textarea value={appealDetails} onChange={(event) => setAppealDetails(event.target.value)} rows={2} placeholder="Appeal details" className="mt-2 w-full rounded-xl border border-[#d7e5d1] bg-white px-3 py-2 text-xs font-normal" /><button onClick={() => void submitAppeal()} className="mt-2 rounded-full border border-[#8db379] px-3 py-1.5 text-[11px] font-bold">Submit appeal</button>{appealSent && <span className="ml-2 font-normal">Appeal received.</span>}</div>}<button onClick={() => void submitComplaint()} className="mt-3 rounded-full border border-[#d5a393] px-4 py-2.5 text-xs font-bold text-[#a45843]">Submit complaint</button></div></div></div><aside className="rounded-[24px] bg-[#edf5e5] p-5"><p className="text-xs font-bold uppercase tracking-[0.16em] text-[#71846f]">Expertise</p><div className="mt-4 flex flex-wrap gap-2">{[...worker.tags, "On-site support", "Safety first"].map((tag) => <span key={tag} className="rounded-full bg-white px-3 py-2 text-xs font-semibold text-[#496052]">{tag}</span>)}</div><div className="my-6 h-px bg-[#d7e5d1]" /><div className="flex items-center gap-3"><div className="grid h-10 w-10 place-items-center rounded-2xl bg-[#d7f477] text-[#395a37]"><Compass size={19} /></div><div><p className="text-sm font-semibold text-[#314a3c]">Works within 25 km</p><p className="mt-0.5 text-xs text-[#78907b]">Live location shared on active jobs</p></div></div><div className="mt-4 flex items-center gap-3"><div className="grid h-10 w-10 place-items-center rounded-2xl bg-white text-[#607d65]"><MessageCircle size={18} /></div><div><p className="text-sm font-semibold text-[#314a3c]">Quick response</p><p className="mt-0.5 text-xs text-[#78907b]">Usually replies within 12 min</p></div></div></aside></div></div></div></div>;
}

export default function Home() {
  const [workforce, setWorkforce] = useState<"Male" | "Female">("Male");
  const [selectedWorker, setSelectedWorker] = useState<(typeof workers)[number] | null>(null);
  const [bookingWorker, setBookingWorker] = useState<(typeof workers)[number] | null>(null);
  const [query, setQuery] = useState("");
  const [activeCategory, setActiveCategory] = useState("All services");
  const [sort, setSort] = useState("Recommended");
  const [mobileMenu, setMobileMenu] = useState(false);
  const [notice, setNotice] = useState("");
  const [publishedWorkers, setPublishedWorkers] = useState<any[]>([]);
  const [locationFilter, setLocationFilter] = useState("All locations");
  const [minPrice, setMinPrice] = useState("");
  const [maxPrice, setMaxPrice] = useState("");
  const [minRating, setMinRating] = useState("0");

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    setWorkforce(params.get("workforce") === "Female" ? "Female" : "Male");
    setQuery(params.get("q") || ""); setActiveCategory(params.get("category") || "All services"); setLocationFilter(params.get("location") || "All locations");
    setMinPrice(params.get("minPrice") || ""); setMaxPrice(params.get("maxPrice") || ""); setMinRating(params.get("minRating") || "0"); setSort(params.get("sort") || "Recommended");
  }, []);
  useEffect(() => {
    const params = new URLSearchParams();
    if (workforce !== "Male") params.set("workforce", workforce); if (query) params.set("q", query); if (activeCategory !== "All services") params.set("category", activeCategory); if (locationFilter !== "All locations") params.set("location", locationFilter);
    if (minPrice) params.set("minPrice", minPrice); if (maxPrice) params.set("maxPrice", maxPrice); if (minRating !== "0") params.set("minRating", minRating); if (sort !== "Recommended") params.set("sort", sort);
    window.history.replaceState({}, "", `${window.location.pathname}${params.toString() ? `?${params.toString()}` : ""}`);
  }, [activeCategory, locationFilter, maxPrice, minPrice, minRating, query, sort, workforce]);

  useEffect(() => { fetch("/api/workers/public").then((response) => response.ok ? response.json() : []).then((items) => setPublishedWorkers(items)).catch(() => setPublishedWorkers([])); }, []);
  const publishedForWorkforce = publishedWorkers.filter((worker) => workforce === "Female" ? worker.gender === "Female" : worker.gender !== "Female");
  const activeWorkers = workforce === "Male" ? [...workers, ...publishedForWorkforce] : [...femaleWorkers, ...femaleAdditionalWorkers, ...publishedForWorkforce];
  const activeCategories = workforce === "Male" ? categories : femaleCategories;
  const filteredWorkers = useMemo(() => {
    const normalized = query.toLowerCase();
    const matches = activeWorkers.filter((worker) => {
      const workerServices = Array.isArray(worker.services) ? worker.services.map((service: any) => service.name || "") : [];
      const searchable = [worker.name, worker.role, worker.city, ...worker.tags, ...workerServices].join(" ").toLowerCase();
      const matchesQuery = !normalized || searchable.includes(normalized);
      const matchesCategory = activeCategory === "All services" || searchable.includes(activeCategory.toLowerCase());
      const numericPrice = Number(String(worker.price).replace(/[^0-9]/g, "")) || 0;
      const numericRating = Number(worker.rating) || 0;
      const matchesLocation = locationFilter === "All locations" || worker.city.toLowerCase().includes(locationFilter.toLowerCase());
      const matchesPrice = worker.price === "Contact" || ((!minPrice || numericPrice >= Number(minPrice)) && (!maxPrice || numericPrice <= Number(maxPrice)));
      const matchesRating = numericRating >= Number(minRating);
      return matchesQuery && matchesCategory && matchesLocation && matchesPrice && matchesRating;
    });
    if (sort === "Top rated") return [...matches].sort((a, b) => Number(b.rating) - Number(a.rating));
    if (sort === "Lowest price") return [...matches].sort((a, b) => Number(a.price.replace(",", "")) - Number(b.price.replace(",", "")));
    return matches;
  }, [activeCategory, activeWorkers, locationFilter, maxPrice, minPrice, minRating, query, sort]);

  const scrollToDirectory = () => document.getElementById("directory")?.scrollIntoView({ behavior: "smooth" });
  const showNotice = (message: string) => { setNotice(message); window.setTimeout(() => setNotice(""), 3200); };

  return <div className="min-h-screen bg-[#f7f9f4] text-[#1c2c2a]">
    <header className="sticky top-0 z-30 border-b border-[#e5ebe1]/80 bg-[#f7f9f4]/90 backdrop-blur-xl"><div className="mx-auto flex h-[76px] max-w-[1240px] items-center justify-between px-5 lg:px-8"><a href="#top" className="flex items-center gap-3"><span className="grid h-10 w-10 place-items-center rounded-[14px] bg-[#203a34] text-[#dff681] shadow-[4px_4px_0_#c4db8e]"><Zap size={20} fill="currentColor" /></span><span className="font-display text-xl font-bold tracking-[-0.05em] text-[#213632]">labrkp<span className="text-[#87a553]">.</span></span></a><nav className="hidden items-center gap-8 text-sm font-semibold text-[#65736e] lg:flex"><a href="#directory" className="transition hover:text-[#203a34]">Find a worker</a><a href="#how-it-works" className="transition hover:text-[#203a34]">How it works</a><a href="#categories" className="transition hover:text-[#203a34]">Categories</a></nav><div className="hidden items-center gap-3 sm:flex"><Link href="/become-a-worker" className="rounded-full px-4 py-2.5 text-sm font-semibold text-[#50635b] transition hover:bg-white">Become a worker</Link><Link href="/admin/verification" className="rounded-full px-3 py-2.5 text-xs font-bold text-[#65736e] transition hover:bg-white hover:text-[#203a34]">Admin login</Link><Link href="/console" className="rounded-full bg-[#203a34] px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-[#37564c]">Worker console</Link></div><button onClick={() => setMobileMenu((value) => !value)} className="grid h-10 w-10 place-items-center rounded-full bg-white text-[#294139] sm:hidden"><Menu size={19} /></button></div>{mobileMenu && <div className="border-t border-[#e5ebe1] bg-[#f7f9f4] px-5 py-4 sm:hidden"><div className="flex flex-col gap-3 text-sm font-semibold text-[#65736e]"><a href="#directory" onClick={() => setMobileMenu(false)}>Find a worker</a><a href="#how-it-works" onClick={() => setMobileMenu(false)}>How it works</a><Link href="/become-a-worker">Become a worker</Link><Link href="/admin/verification">Admin login</Link><Link href="/console">Worker console</Link></div></div>}</header>

    <main id="top">
      <section className="mx-auto max-w-[1240px] px-5 pb-12 pt-8 lg:px-8 lg:pt-12"><div className="relative overflow-hidden rounded-[32px] bg-[#1d3430] px-6 py-10 text-white shadow-[0_22px_60px_rgba(30,54,45,0.14)] sm:px-10 lg:min-h-[535px] lg:px-14 lg:py-14"><div className="pointer-events-none absolute -right-20 -top-28 h-80 w-80 rounded-full border-[38px] border-[#2c4a42]/70" /><div className="pointer-events-none absolute -bottom-32 left-[38%] h-80 w-80 rounded-full border-[1px] border-[#7d9b62]/25" /><div className="relative z-10 grid items-center gap-12 lg:grid-cols-[1.05fr_0.95fr]"><div className="max-w-[630px]"><div className="mb-6 inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/[0.07] px-3.5 py-2 text-xs font-semibold text-[#dceacb]"><Sparkles size={14} className="text-[#d8f479" /> The trusted way to get things done</div><div className="mb-5 inline-flex rounded-full border border-white/15 bg-white/[0.07] p-1"><button onClick={() => { setWorkforce("Male"); setActiveCategory("All services"); }} className={`rounded-full px-4 py-2 text-xs font-bold transition ${workforce === "Male" ? "bg-[#d8f479] text-[#263d32]" : "text-white/60 hover:text-white"}`}>Male Workforce</button><button onClick={() => { setWorkforce("Female"); setActiveCategory("All services"); }} className={`rounded-full px-4 py-2 text-xs font-bold transition ${workforce === "Female" ? "bg-[#d8f479] text-[#263d32]" : "text-white/60 hover:text-white"}`}>Female Workforce</button></div><h1 className="max-w-[610px] font-display text-[48px] font-semibold leading-[0.98] tracking-[-0.06em] text-white sm:text-[68px]">Skilled help.<br /><span className="text-[#d8f479]">On your terms.</span></h1><p className="mt-6 max-w-[500px] text-base leading-7 text-[#b8cbc0] sm:text-lg">Book verified local professionals for the work that keeps your world moving — from a quick fix to a full solar setup.</p><div className="mt-8 flex flex-wrap items-center gap-4 text-sm text-[#d0ddd5]"><span className="flex items-center gap-2"><span className="grid h-6 w-6 place-items-center rounded-full bg-[#d8f479] text-[#2a4538]"><Check size={13} strokeWidth={3} /></span> Verified workers</span><span className="flex items-center gap-2"><span className="grid h-6 w-6 place-items-center rounded-full bg-[#d8f479] text-[#2a4538]"><Check size={13} strokeWidth={3} /></span> Transparent pricing</span></div></div><div className="relative mx-auto w-full max-w-[430px]"><div className="absolute -left-7 top-8 hidden rounded-2xl border border-white/10 bg-[#304a43] px-4 py-3 shadow-xl sm:block"><div className="flex items-center gap-2"><span className="grid h-8 w-8 place-items-center rounded-xl bg-[#d8f479] text-[#294139]"><ShieldCheck size={16} /></span><div><p className="text-[10px] uppercase tracking-[0.15em] text-white/50">All workers</p><p className="text-sm font-semibold">Background checked</p></div></div></div><div className="relative overflow-hidden rounded-[28px] border-8 border-white/10 bg-[#b3d36b] shadow-2xl"><img src={SOLAR_IMAGE} alt="Solar technician at work" className="h-[350px] w-full object-cover lg:h-[400px]" /><div className="absolute inset-0 bg-gradient-to-t from-[#172e2a]/75 via-transparent to-transparent" /><div className="absolute bottom-5 left-5 right-5 flex items-end justify-between"><div><p className="text-xs font-bold uppercase tracking-[0.16em] text-[#d8f479]">Popular right now</p><p className="mt-1 font-display text-2xl font-semibold">Solar & energy</p></div><span className="grid h-11 w-11 place-items-center rounded-full bg-[#d8f479] text-[#203a34]"><ArrowRight size={18} /></span></div></div><div className="absolute -bottom-7 -right-2 rounded-2xl bg-white p-3 text-[#233d36] shadow-xl sm:-right-6"><div className="flex items-center gap-2"><div className="flex -space-x-2">{workerImages.map((image) => <img key={image} src={image} alt="" className="h-8 w-8 rounded-full border-2 border-white object-cover" />)}</div><div><p className="font-display text-lg font-bold leading-none">2,400+</p><p className="mt-1 text-[10px] font-semibold uppercase tracking-[0.13em] text-[#829087]">local pros</p></div></div></div></div></div><div className="relative z-10 mt-12 grid gap-3 rounded-[22px] bg-white p-2.5 shadow-[0_18px_35px_rgba(14,33,29,0.22)] sm:grid-cols-[1.4fr_1fr_0.75fr_auto] sm:rounded-full"><label className="flex items-center gap-3 rounded-full px-4 py-3 sm:border-r sm:border-[#edf0eb]"><Search size={18} className="shrink-0 text-[#7c8e83]" /><input value={query} onChange={(event) => setQuery(event.target.value)} onKeyDown={(event) => event.key === "Enter" && scrollToDirectory()} placeholder="What do you need help with?" className="w-full bg-transparent text-sm text-[#294139] outline-none placeholder:text-[#94a19a]" /></label><button onClick={() => { setActiveCategory("All services"); scrollToDirectory(); }} className="flex items-center justify-between gap-3 rounded-full border-t border-[#edf0eb] px-4 py-3 text-left text-sm text-[#6d7e76] sm:border-t-0 sm:border-r"><span className="flex items-center gap-3"><MapPin size={17} className="text-[#7c8e83]" />Choose location</span><ChevronDown size={16} /></button><button onClick={scrollToDirectory} className="flex items-center justify-between gap-3 rounded-full border-t border-[#edf0eb] px-4 py-3 text-left text-sm text-[#6d7e76] sm:border-t-0 sm:border-r"><span className="flex items-center gap-3"><SlidersHorizontal size={17} className="text-[#7c8e83]" />All services</span><ChevronDown size={16} /></button><button onClick={scrollToDirectory} className="rounded-full bg-[#d8f479] px-6 py-3.5 text-sm font-bold text-[#263d32] transition hover:bg-[#e7ff9a]">Find help</button></div></div></section>

      <section id="categories" className="mx-auto max-w-[1240px] px-5 py-10 lg:px-8"><div className="flex items-end justify-between"><div><p className="text-xs font-bold uppercase tracking-[0.2em] text-[#8a9b8f]">Browse by need</p><h2 className="mt-2 font-display text-3xl font-semibold tracking-[-0.04em] text-[#213632] sm:text-4xl">{workforce === "Female" ? "Female services by category" : "Start with a category"}</h2></div><button onClick={() => { setActiveCategory("All services"); scrollToDirectory(); }} className="hidden items-center gap-2 text-sm font-semibold text-[#5d765a] sm:flex">View all <ArrowRight size={15} /></button></div><div className="mt-7 grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-4">{activeCategories.map((category) => <div key={category.name} className="group rounded-[22px] border border-[#e5ebe1] bg-white p-4 text-left transition hover:-translate-y-1 hover:border-[#b7cd9a] hover:shadow-lg"><button onClick={() => { setActiveCategory(category.name); scrollToDirectory(); }} className="w-full text-left"><span className={`grid h-12 w-12 place-items-center rounded-2xl text-2xl ${category.tint}`}>{category.icon}</span><p className="mt-4 text-sm font-bold text-[#294139]">{category.name}</p><p className="mt-1 text-[11px] text-[#8a9891]">{category.count}</p></button>{"services" in category && Array.isArray(category.services) && <div className="mt-3 flex flex-wrap gap-1.5">{category.services.map((service: string) => <button key={service} onClick={() => { setQuery(service); setActiveCategory("All services"); scrollToDirectory(); }} className="rounded-full bg-[#f3f7ed] px-2.5 py-1 text-[10px] font-semibold text-[#587060] transition hover:bg-[#e4f1cc]">{service}</button>)}</div>}</div>)}</div></section>

      <section id="directory" className="mx-auto max-w-[1240px] scroll-mt-24 px-5 py-12 lg:px-8"><div className="flex flex-col justify-between gap-5 sm:flex-row sm:items-end"><div><div className="flex items-center gap-2 text-xs font-bold uppercase tracking-[0.2em] text-[#8a9b8f]"><span className="h-2 w-2 rounded-full bg-[#9bc45d]" />{workforce} workforce directory</div><h2 className="mt-2 font-display text-3xl font-semibold tracking-[-0.04em] text-[#213632] sm:text-4xl">Find your people</h2><p className="mt-2 text-sm text-[#788780]">{filteredWorkers.length} verified pros ready to help across KP.</p></div><div className="flex flex-wrap items-center gap-2"><select aria-label="Filter by location" value={locationFilter} onChange={(event) => setLocationFilter(event.target.value)} className="rounded-full border border-[#dce5d9] bg-white px-3 py-2.5 text-xs font-semibold text-[#52675d] outline-none"><option>All locations</option>{["Peshawar", "Kohat", "Mardan", "Abbottabad", "Swat", "Nowshera", "Bannu", "Charsadda", "Mansehra"].map((city) => <option key={city}>{city}</option>)}</select><select aria-label="Minimum rating" value={minRating} onChange={(event) => setMinRating(event.target.value)} className="rounded-full border border-[#dce5d9] bg-white px-3 py-2.5 text-xs font-semibold text-[#52675d] outline-none"><option value="0">Any rating</option><option value="4">4+ stars</option><option value="4.5">4.5+ stars</option><option value="4.8">4.8+ stars</option></select><select aria-label="Price range" value={`${minPrice}-${maxPrice}`} onChange={(event) => { const [min, max] = event.target.value.split("-"); setMinPrice(min); setMaxPrice(max); }} className="rounded-full border border-[#dce5d9] bg-white px-3 py-2.5 text-xs font-semibold text-[#52675d] outline-none"><option value="-">Any price</option><option value="0-1000">Up to Rs. 1,000</option><option value="1000-2000">Rs. 1,000–2,000</option><option value="2000-">Rs. 2,000+</option></select><select aria-label="Filter by category" value={activeCategory} onChange={(event) => setActiveCategory(event.target.value)} className="rounded-full border border-[#dce5d9] bg-white px-3 py-2.5 text-xs font-semibold text-[#52675d] outline-none"><option>All services</option>{activeCategories.map((category) => <option key={category.name}>{category.name}</option>)}</select><select aria-label="Sort workers" value={sort} onChange={(event) => setSort(event.target.value)} className="rounded-full border border-[#dce5d9] bg-white px-3 py-2.5 text-xs font-semibold text-[#52675d] outline-none"><option>Recommended</option><option>Top rated</option><option>Lowest price</option></select></div></div><div className="mt-7 grid grid-cols-2 gap-3 md:grid-cols-3 lg:grid-cols-4">{filteredWorkers.map((worker) => <WorkerCard key={worker.id} worker={worker} onOpen={setSelectedWorker} />)}</div>{filteredWorkers.length === 0 && <div className="mt-7 rounded-[26px] border border-dashed border-[#cfdacb] bg-white py-16 text-center"><p className="font-display text-xl font-semibold text-[#294139]">No matching workers yet</p><p className="mt-2 text-sm text-[#829087]">Try a broader service or search term.</p></div>}<div className="mt-8 flex flex-col items-center justify-between gap-4 rounded-[24px] bg-[#eaf3dc] px-6 py-5 sm:flex-row"><div className="flex items-center gap-3"><div className="grid h-10 w-10 place-items-center rounded-2xl bg-[#d6f477] text-[#355d3d]"><Bell size={18} /></div><p className="text-sm text-[#526853]"><strong className="text-[#294139]">Need something specific?</strong> Tell us what you need and we’ll match you.</p></div><button onClick={() => showNotice("Tell us what you need — matching is coming next.")} className="flex items-center gap-2 rounded-full bg-[#294139] px-5 py-2.5 text-sm font-semibold text-white">Request a match <ArrowRight size={15} /></button></div></section>

      <section id="how-it-works" className="border-y border-[#e5ebe1] bg-white"><div className="mx-auto max-w-[1240px] px-5 py-16 lg:px-8"><div className="grid gap-10 lg:grid-cols-[0.8fr_1.2fr] lg:items-end"><div><p className="text-xs font-bold uppercase tracking-[0.2em] text-[#8a9b8f]">Simple by design</p><h2 className="mt-2 max-w-sm font-display text-3xl font-semibold tracking-[-0.04em] text-[#213632] sm:text-4xl">From “I need help” to “all sorted.”</h2><p className="mt-4 max-w-sm text-sm leading-6 text-[#788780]">A clear booking flow, real worker profiles and no awkward guesswork.</p></div><div className="grid gap-4 sm:grid-cols-3">{[{ number: "01", title: "Tell us what you need", body: "Search by service, skill, name or your city." }, { number: "02", title: "Choose with confidence", body: "Compare verified profiles, work history and pricing." }, { number: "03", title: "Get it done", body: "Book a time, follow the ETA and pay when complete." }].map((step) => <div key={step.number} className="rounded-[22px] bg-[#f3f7ed] p-5"><span className="font-display text-3xl font-semibold text-[#b5c99a]">{step.number}</span><h3 className="mt-8 text-base font-bold text-[#294139]">{step.title}</h3><p className="mt-2 text-sm leading-6 text-[#7a8a80]">{step.body}</p></div>)}</div></div></div></section>

      <div className="mx-auto max-w-[1240px] px-5 pb-10 lg:px-8"><div className="flex flex-col items-center justify-between gap-4 rounded-[24px] bg-[#eaf3dc] px-6 py-6 text-center sm:flex-row sm:text-left"><div><p className="text-xs font-bold uppercase tracking-[0.16em] text-[#789159]">Grow with LABRKP</p><p className="mt-1 text-sm text-[#526853]"><strong className="text-[#294139]">Want to offer your skills?</strong> Join our verified workforce.</p></div><Link href="/become-a-worker" className="flex items-center gap-2 rounded-full bg-[#294139] px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-[#355d4d]">Join us as a worker <ArrowRight size={15} /></Link></div></div>
      <footer className="mx-auto flex max-w-[1240px] flex-col justify-between gap-5 px-5 py-10 text-sm text-[#819087] sm:flex-row sm:items-center lg:px-8"><div className="flex items-center gap-3"><span className="grid h-8 w-8 place-items-center rounded-xl bg-[#203a34] text-[#dff681]"><Zap size={16} fill="currentColor" /></span><span className="font-display font-bold text-[#294139]">labrkp.</span><span>© 2026 · Built for better work.</span></div><div className="flex gap-5"><a href="#top" className="hover:text-[#294139]">Privacy</a><a href="#top" className="hover:text-[#294139]">Safety</a><a href="#top" className="hover:text-[#294139]">Support</a></div></footer>
    </main>

    {selectedWorker && !bookingWorker && <WorkerDetail worker={selectedWorker} onClose={() => setSelectedWorker(null)} onRatingUpdated={(summary) => setSelectedWorker((current) => current ? { ...current, rating: summary.rating, reviews: summary.reviews } : current)} onBook={() => { setBookingWorker(selectedWorker); setSelectedWorker(null); }} />}
    {bookingWorker && <BookingModal worker={bookingWorker} onClose={() => setBookingWorker(null)} />}
    {notice && <div className="fixed bottom-5 left-1/2 z-[60] flex -translate-x-1/2 items-center gap-3 rounded-full bg-[#203a34] px-5 py-3 text-sm font-semibold text-white shadow-2xl"><Check size={16} className="text-[#d8f479]" />{notice}</div>}
  </div>;
}
