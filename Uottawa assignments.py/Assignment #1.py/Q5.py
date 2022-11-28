#############################################################
#Anthony Le; 300287511
#Assignment 1, Question 5
# october 21, 2022

#############################################################

import random
p = int(input('How many people are playing?: '))
n = int(input(" what range do you want to play with?: "))
n
mynames = []
guesses = []
while p < 0:
    p = int(input('How many people are playing?: '))

for i in range (0, p):
    x = random.randint(1, n)
    print('What is your name, Player', i + 1, '?:', end = ' ')
    name = str(input(''))
    mynames.append(name)
    g_count = 1
    print('Starting game for', name)
    g = int(input('Enter your guess here:'))
    guess = False
    while guess == False:
        if g > x:
            print('The number is too big!')
            g = int(input('Enter your guess here:'))
            g_count += 1
        if g < x:
            print('The number is too small!')
            g = int(input('Enter your guess here:'))
            g_count += 1
        if g == x:
            print('You guessed the number in', g_count, 'tries!')
            guesses.append(g_count)
            break
            


minval = min(guesses)
minnum = guesses.index(minval)
guessval = guesses [minnum]
winner = mynames [minnum]

win = print('The winner is', winner,'for guessing the number in',guessval,'tries!')




                
        


