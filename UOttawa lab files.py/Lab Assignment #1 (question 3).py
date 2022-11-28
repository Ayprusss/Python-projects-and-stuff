

print('A linear function is as follows: y = mx + b')
m = int(input ('Enter the slope value of the function (m): '))
b = int(input ('Enter the y-intercept value of the function (b): '))
x = int(input ('Enter the x-value of a set of coordinates (x): '))
y = int(input ('Enter the y- value of a set of coordinates (y): '))

y_value = (m * x) + b


if y_value == y:
    print('The coordinate is on the line of the function.')

if y_value > y and x < 0:
    print ('the coordinate is on the left side of the function.')
if y_value < y and x < 0:
        print ('the coordinate is on the left side of the line.')
if y_value > y and x > 0:
        print ('the coordinate is on the right side of the function.')
if y_value < y and x > 0:
        print ('the coordinate is on the right side of the function')




