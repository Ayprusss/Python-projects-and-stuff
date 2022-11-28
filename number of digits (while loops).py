# A program to receive an non-negative integer and print out the number of digits in that integer. 

#if input is = 68282; output == 5

n = int(input('Enter an non-negative integer: '))

digit_count = 0  #sum plate; accumulates the sum of numbers. accumulators

if n == 0:      # code made to take boundary values and values that may break the cde excepted. 
    digit_count = 1

while n != 0:
    digit_count = digit_count + 1
    n = n // 10
print('the number of digits = ', digit_count)



