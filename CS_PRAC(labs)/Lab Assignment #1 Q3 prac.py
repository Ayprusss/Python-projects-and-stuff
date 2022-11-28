m = int(input('Enter the slope of the equation: '))
b = int(input('Enter the y-intercept of the equation: '))
x = int(input('Enter the x-value of a coordinate: '))
y = int(input('Enter the y-value of a coordinate: '))

#must check position of y-value.


eqnx = (y - b) / m

if eqnx == x:
    print('point is one the line.')

if eqnx > x:
    print('point is on the right side of line.')
elif eqnx < x:
    print('point is on the left side of the line. ')