n = int(input('Enter positive integer n: '))
import math

def is_complete(n):
    divisors = []
    m = int(math.sqrt(n)) + 1
    for l in range(1, n):
        if n % l == 0:
            divisors.append(l)
    divisorsum = sum(divisors)
    
    if divisorsum != n:
        return False
    else:
        return True

if is_complete(n):
    print('The number is complete.')
else:
    print('The number is not complete.')



