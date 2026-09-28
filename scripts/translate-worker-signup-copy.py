from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/WorkerSignup.tsx')
s=p.read_text()
replacements={
'Apni skills, city aur experience share karein. Verification ke baad customers aapko directly book kar sakenge.':'Share your skills, city, and experience. Once verified, customers can book you directly.',
'Please complete all required fields and accept verification consent.':'Please complete all required fields and accept the verification consent.',
'LABRKP team verification ke baad aapka profile KP workforce directory mein publish hoga. Admin panel mein request open karke Approve ya Reject karein.':'The LABRKP team will review your profile and publish it in the KP workforce directory after verification. An administrator can approve or reject your application from the admin panel.',
'Only KP cities are currently available on LABRKP. Other skills can be proposed and reviewed by admin.':'Only KP cities are currently available on LABRKP. You may propose other skills for admin review.',
'Your profile is published only after verification.':'Your profile will be published only after verification.',
'Set your services, rates and availability after approval.':'After approval, you can manage your services, rates, and availability.'
}
for old,new in replacements.items():
    if old not in s: raise SystemExit(f'missing copy: {old}')
    s=s.replace(old,new)
p.write_text(s)
