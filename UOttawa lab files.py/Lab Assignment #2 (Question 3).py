n = int(input('Enter a non-negative integer: '))

if n < 0: 
   print (' A postive integer must be inputed. ')
   quit()

new_int = 0

while n != 0:
   digit = n % 10
   new_int = (new_int* 10) + digit
   n //= 10

print('the reversed number is:', new_int)
