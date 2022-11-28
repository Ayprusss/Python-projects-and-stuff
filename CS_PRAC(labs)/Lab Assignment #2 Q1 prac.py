a = int(input('Enter a non-negative integer: '))
sum = 0


print('divisors are:', end = '')

for i in range (1, a):
    divisor = a % i
    if divisor == 0:
        print(i, end = ',')
        sum = sum + i
print(a, end = '')
sum = sum + a
print('')

print('sum of divisors:', sum)

