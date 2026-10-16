x = float(input('Enter weight(kg): '))
y = float(input('Enter Half-life(h): '))
z = float(input('Enter Target_concentration:  '))
w = input('Enter Drug_name: ').title().strip()

VD_TABLE = {
    'Warfarin':     0.14,
    'Digoxin':      7.0,
    'Theophylline': 0.5,
    'Gentamicin':   0.25,
    'Metformin':    1.0,
}

if w in VD_TABLE:
   vd = x * VD_TABLE[w]
   ld = vd * z
   k = 0.693 / y
   md = k * vd * z * 12
   steady_state = 5 * y

   print(f"Volume of Distribution (L): {vd:.2f}")
   print(f"Loading Dose (mg): {ld:.2f}")
   print(f"Maintenance Dose (mg) every 12h: {md:.2f}")
   print(f"Steady state reached in ~{steady_state:.1f} hours")

else: 
   print('Drug not found')