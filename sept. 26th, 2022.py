from operator import truediv


n =int(input('Enter a positive integer: '))

# pick 200 as input
# 1 2 4 5 8 10 20 25 40 50 100 200

prime = True 

m = int(math.sqrt(n)) +  1

m = n // 2
for i in range(2,n):
    if n % i == 0:
        prime = False
        break 

if prime and n != 1:
    print (n, 'is a prime number.')
else:
    print(n, 'is not a prime number.')



# Equivalent while loop that works.

 # , // 2

i = 2
while i * i < n:
    if n % i == 0:
        prime = False
        break
    i = i + 1