# Question 2: three variables, and do quadratic equation: show if equation has no roots, one roots and 2 roots.

print('a parabolic function contain the coefficients: ax^2-bx+c')

a = int(input('Enter the first coefficient (a) '))
b = int(input('Enter the second coefficient (b) '))
c = int(input('Enter the third coefficient (c)'))

function = b ** 2 - 4 * a * c

if function > 0:
    print('the function has more than two roots.')
elif function == 0:
    print('The function has only one root.')
elif function < 0:
    print('The function has no roots.')
