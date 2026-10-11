x = int(input('Enter FastingGlucose: ').strip())
y = int(input('Enter Postmeal_Glucose: ').strip())

parameters = {
    'FG': (100, 126),
    'PMG': (140, 200)
}

if x < parameters['FG'][0]:
    print('Normal')
elif x >= parameters['FG'][1]:
    print('Diabetic')
else:
    print('Prediabetic')

if y < parameters['PMG'][0]:
    print('Normal')
elif y >= parameters['PMG'][1]:
    print('Diabetic')
else:
    print('Prediabetic')
            


