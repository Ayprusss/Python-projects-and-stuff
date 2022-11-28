# Online Python - IDE, Editor, Compiler, Interpreter

# A program that receives a positive integer and prints out if the number is prime or not
# input = 57     output = The number is not prime
# input = 37     output = The number is prime

n = int(input('Enter a positive integer: '))
is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:    # is_prime == True
    print('The number is prime', end = ', ')
else:
    print('The number is not prime', end = ', ')
    
print('end of the program')
