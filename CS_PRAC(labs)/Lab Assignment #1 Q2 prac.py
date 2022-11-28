# use of determinants.
import math

a = int(input('Enter your first coefficient: '))
b = int(input('Enter your second coefficient: '))
c = int(input('Enter your third coefficient: '))

determinant = b ** 2 - (4 * a * c)

if determinant > 0:
    root1 = ((-1) * b + (determinant) ** (1/2)) / (2 * a)
    print('root 1:', root1)
    root2 = ((-1) * b - (determinant) ** (1/2)) / (2 * a)
    print('root 2:', root2)

if determinant == 0:
    root1 = ((-1) * b + (determinant) ** (1/2)) / (2 * a)
    print('root1:', root1)

if determinant < 0:
    print('there are no roots. ')