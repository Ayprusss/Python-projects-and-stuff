import math
from tempfile import tempdir
w = int(input('What is the width of the rectangle?: '))
l = int(input('what is the length of the rectangle?: '))

def squares(x,y):
    if x == y:
        return x * (x + 1)*(2*x + 1) // 6
    if x < y or x > y:
        tempvalue = l
        x = y
        y = tempvalue # done so that l has higher value.
        return ((x * (x + 1) * (2 * x + 1) // 6 + (y - x) * x * (x + 1)// 2))
    
print('total number of squares = ', squares(l,w)) # total includes squares and rectangles 
        
def rectangles(x,y):
    return (x * y * (y + 1) * (x + 1)) // 4

print('total number of rectangles=', rectangles(l,w))

# to find total number of rectangles that are not squares.
print("total number of rectangles that aren't squares", abs(squares(l,w) - rectangles(l,w)))


