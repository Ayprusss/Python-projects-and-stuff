# create program that can check for prime numbers in between range of a and b 
a = int(input('Enter your first positive integer: '))
b = int(input('Enter a greater second positive integer: ')) 

print ('your prime numbers are:', end = ' ')
prime_list_num = 0
for n in range(a,b + 1):

    prime = True
    for j in range(2, n):
        remainder = n % j 
        if remainder == 0:
            prime = False
            break
    if prime:
        print (n, end = ' ')
        prime_list_num += 1
    if n == 1:
        prime == False
        
print (end = '\n')

print ('The total number of prime numbers within that range:', prime_list_num)

