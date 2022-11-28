import math

def is_prime(n):
    '''
    n is a positive integer
    The function is going to check if this number is prime or not
    '''
    m = int(math.sqrt(n)) + 1
    if n == 1:
        return False
    
    for i in range(2, m):
        if n % i == 0:
            return False

    return True

# main part of the program
n = int(input('Enter an even integer greater than 2: '))
m = n // 2

for i in range(2, m + 1):
    if is_prime(i) and is_prime(n - i):
        print(n, ' =', i, '+', n - i)
        break





    
