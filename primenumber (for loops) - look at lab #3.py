# a program that receives a positive integer and prints out if the number is a prime or not 

# input = 57 out = the number is not prime

# input = 37        output = the number is prime.

# this is a decision problem

# keyword for for loops = from a to b

n =int(input ('Enter a positive integer: '))
is_prime = True

for i in range(2, n):
    if n % i == 0:          # can also optimize it by checking with the sqrt of the number x
        is_prime = False
        break       #REMEMBER: if the output is known (in this case, if we know if the number is or is not a prime; always put a break to end the loop.)


if is_prime:        # is_prime == True; same thing if you just say is_prime; it's a boolean.
    print('the number is prime', end = ', ')
else:
    print('The number is prime', end = ' ')