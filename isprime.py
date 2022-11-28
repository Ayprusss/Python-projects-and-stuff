
n = int(input('Enter an integer greater than 2:'))

def prime(n):
    primes = []
    for x in range(1,n + 1):
        prime = True
        for j in range(2, x):
            remainder = n % j 
            if remainder == 0:
                prime = False
                break
        
        if n == 1:
            prime == False
        if prime:
            primes.append(x)
        
    return primes


print(prime(n))

for a in (prime(n)):
    sum = False
    for b in (prime(n)):
        if a + b == n:
            print(n, '=', a, '+', b)
            sum = True
    if sum:
        break