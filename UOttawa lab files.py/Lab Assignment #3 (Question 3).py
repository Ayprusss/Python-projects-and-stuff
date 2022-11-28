
a = int(input('Enter your first number here: '))

import random 
x = random.randint(1,a)
m = 1
c = 1

# response = [y, n]
while m != 0:       #while loop for the number of inputs to be given to the user?
    print('Game is starting' + '...')
    d = int(input('Enter your guess here: '))
    m = m - 1
    while d < 0:
        d = int(input('Enter your guess here: '))   # practice inputs in loops.
    while c != 0:
        if d < x :
            print('number is too low.')
            d = int(input('Enter another guess: '))
        if d > x:
            print('number is to big.')
            d = int(input('Enter another guess: '))
        if d == x:
            print('you guessed the right number!!')
            c = c - 1.
        if d < 1:
            print('value is smaller than the range of 1 to a.')
            d = int(input('Enter another guess: '))
        if d > a:
            print('value is bigger than the range of 1 to a.')
            d = int(input('Enter another guess: '))

    while c == 0:
        q = str(input(' Would you like to play again?: ')) # problem; if the x value equals 1 in the next loop; or the base a, it will continue to loop that value. 
        if q == 'y':
            c = c + 1
            m = m + 1
            x = random.randint(1, a)
        elif q == 'n':
            print('Thanks for playing!')
            quit()