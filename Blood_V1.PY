X = input('Enter Blood Group: ').upper().strip()

can_recieve_from = {
    'O-': ['O-'],
    'O+': ['O+','O-'],
    'A+': ['A+','A-','O+','O-'],
    'A-': ['A-','O-'],
    'B+': ['B+','B-','O+','O-'],
    'B-': ['B-','O-'],
    'AB+': ['AB+','AB-','A+','A-','B+','B-','O+','O-'],
    'AB-': ['AB-','B-','A-','O-']
}

if X in can_recieve_from:
    compatible = can_recieve_from[X]
    all_types = ['O-','O+','A+','A-','B+','B-','AB+','AB-']
    incompatible = [t for t in all_types if t not in compatible]
    print(f"Blood Group : {X}")
    print(f"can recieve from: {compatible}")
    print(f"cannot recieve from : {incompatible}")
else:
    print('invalid blood group')



