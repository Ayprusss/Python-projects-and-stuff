# program that receives  non-negative integer and prints out the sum of the digits.

# input = 682 output = 16

n = int(input('Enter an non-negative integer: '))

sum_digits = 0  #sum plate; accumulates the sum of numbers. accumulators

if n == 0:      # code made to take border values and values that may break the cde excepted; but sometimes, border values do not affect the function whatsoever.
    sum_digits = 1

while n != 0:
    r = n % 10
    sum_digits = sum_digits + r 
    n = n // 10         # order is important; in this case; if floor division goes first; number is being divided and then remainder is found. Values are lost. LOOK OVER THE ORDER OF FUNCTIONS
print('the sum of  the digits = ', sum_digits)