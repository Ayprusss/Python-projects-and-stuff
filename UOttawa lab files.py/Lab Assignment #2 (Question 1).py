# write a pgrogram that receives a positive integer - your output should be all divisors of this integer in a comma seperated format as shown and the sum of all divisors.
number = int(input ('Enter an integer here: '))  # something that has to do with modulus

divisor = 0

divisor_sum = 0

while divisor <= number:
    divisor = divisor + 1
    remainder = number % divisor  
    if remainder == 0:
        divisor_sum = divisor_sum + divisor
        print (str(divisor)+',', end = '') 
    if divisor == number and remainder == 0:
        print (' ')

print ('the sum of all divisors is =', str(divisor_sum))

# end = ',')1