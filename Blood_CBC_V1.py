x = input('Enter Sex (M/F): ').upper().strip()
y = float(input('Enter hb(Hemoglobin): '))
z = float(input('Enter WBC count: '))
w = float(input('Enter Platelets count: '))

parameters = {
    'hb': {'M': (13.5, 17.5), 'F': (12.0, 15.5)},
    'WBC': (4.0, 11.0),
    'Platelets': (150, 450)
}

if x in ['M', 'F']:
    hb_range = parameters['hb'][x]
    if hb_range[0] <= y <= hb_range[1]:
        print(' hb = Normal range')
    else:
        print(' hb = Abnormal range')

    if parameters['WBC'][0] <= z <= parameters['WBC'][1]:
        print('WBC = Normal range')
    else:
        print('WBC = Abnormal range')

    if parameters['Platelets'][0] <= w <= parameters['Platelets'][1]:
        print('Platelets = Normal range')
    else:
        print('Platelets = Abnormal range')
else:
    print('Invalid sex')
    exit()

