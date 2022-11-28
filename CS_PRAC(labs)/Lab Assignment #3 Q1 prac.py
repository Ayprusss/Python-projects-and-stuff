a = int(input('Enter the first number of the range: '))
b = int(input('Enter the last number of the range: '))

print('primes: ', end = ' ')
counter = 0
for i in range(a,b):
    prime = True

    for j in range(2, i):
        divisor = i % j
        if divisor == 0:
            prime = False
            break
    if prime:
        counter += 1
        print(i, end = ', ')
    
print('\n')
print('number of primes:', counter)