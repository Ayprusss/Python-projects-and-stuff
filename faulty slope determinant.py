# Question 3: four variables: slope variable, b variable (y=int); x and y variable. see if point is on left side, right side or line or on it.

print('A linear function is as follows: y = mx + b')
m = int(input ('Enter the slope value of the function (m): '))
b = int(input ('Enter the y-intercept value of the function (b): '))
y = int(input ('Enter the y- value of a set of coordinates (y): '))
x = int(input ('Enter the x-value of a set of coordinates (x): '))

y_value = (m * x) + b

if y_value == y:
    print('The y-coordinate is on the line of the function.')

if y_value > y:
    print ('the y-coordinate is above the line.')
if y_value < y:
    print('the y-coordinate is below the line.')

x_value = (y - b) / m

if x_value == x:
    print ('the x-coordinate is on the line of the function.')
elif x_value > x: 
    print ('the x-coordinate is to the right of the line.')
elif x_value < x:
    print ('the x-coordinate is to the left of the line')