# Nesting loops

a = 0
for i in range(1, 11):
    for j in range(1,10):
        print(i,  '*', j, '=' , i * j, end = ', ')
    print('')
        # nesting loop occurs when a for loop is in another loop. Repeats ten times for the ten iteraions
        
    