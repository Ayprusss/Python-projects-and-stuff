weight = int(input ('what is your weight? : '))
value =(input ('is your weight in (k)g or in (L)bs? : '))


if value.upper() == 'K':
    converted = weight / 0.45
    print('Weight in Lbs', converted)
else:
    converted = weight * 0.45
    print ( 'your weight in Kg is :', converted)



