temperature = 25

if temperature > 30: 
    print('it sure is hot today')
    print('drink plenty of water')
elif temperature > 20: # (20, 30]
    print(" it's a cool day")
elif temperature > 10: # (10, 20]
    print('it is a cold day')
else:
    print("it's cold")