# Question 2: write program that receives coefficients of quadratic equation and print out roots of quadratic equation. coefficients and answers are all float. recall quadratic equation has no, one or two roots.

print ('parabolic functions tend to be in the form of : ax^2 + bx + c. ')
a = float(input ('Enter your first coefficient here (a): '))
b = float(input ('Enter your second coefficient here (b): '))
c = float(input('Enter your third coefficient here (c): '))

#First, determine whether or not the function has any roots.
        #use the determinant formula to figure out if roots are present.

determinant = (b ** 2) - (4 * a * c)
if determinant > 0:
    print ('the function has two roots. ')
elif determinant == 0:
    print ('the function has onle one root.')
else:
    print (' the function has no zeros. ')

if determinant > 0:
    root_1 = ((-1 * b) + (determinant ** .5)) / (2 * a)
    root_2 = ((-1 * b) - (determinant ** .5)) / (2 * a)
    print ('your first root is', root_1)
    print ('your second root is', root_2)
if determinant == 0:
    root_only = ((-1 * b) + (determinant ** .5)) / (2 * a)
    print ('your only root is', root_only)
    