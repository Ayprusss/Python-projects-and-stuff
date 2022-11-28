
n = int(input('Enter a positive integer: '))

sum = 0

print('Divisors =', end = ' ')
for i in range(1, n):
    if n % i == 0:
        sum += i #same as sum = sum + i
        print(i, end = ', ')

sum += n
print(n)
print('Sum of divisors =', sum)
        
