a = int(input('Enter the first number in the range: '))
b = int(input('Enter the end number for the range: '))

primecounter = 0
Prime = True
print ('prime numbers are: ', end = '')
for i in range (a, b + 1):
    Prime = True
    for j in range(2, i):
        remainder = i % j 
        if remainder == 0:
            Prime = False
            break
    if Prime:
        print(i, end = ' ') 
        primecounter += 1

print('\n')
print('number of primes:', primecounter)
