#############################################################
#Anthony Le; 300287511
#Assignment 2, Question 21
# November 9, 2022

#############################################################
import random
colours = ['Red', 'Yellow', 'Blue', 'Green', 'Orange', 'Pink', 'Purple', 'Cyan', 'Silver', 'Teal']

answer = []
numbers = []
penalties = 0
i = 0
gameWon = False
gameOver = False

while i != 4: # MAKE INTO METHOD LATER
    y = random.randint(0, len(colours) - 1)
    if y not in numbers:
        numbers.append(y)
        i += 1

for j in range(0, len(numbers)):
    l = numbers[j]
    col = colours[l]
    answer.append(col)

print('colours for game: ', answer)
name = str(input('What is your name?: '))
print('\n','Welcome to Master-Mind,', name,'!!')
print('The code maker is here. The available colours are:')
print('\n', ', '.join(colours))
print('\n', 'You have a total of 15 guesses and a total of 5 penalties are allowed. Try to avoid these penalties.')
print('The code maker has chosen four colours. You may now begin guessing,', name)

for n in range(0, 16):
    print('')
    print('Enter guess no.', n + 1, ': ', end = '')
    guess = list(map(str, input('').split()))
    print(guess)
    whites = 0
    blacks = 0
    penalized = False
    sum = n + 1

    for p in range(0, len(answer)): # MAKE INTO METHOD LATER
        ans1 = answer[p]
        for o in range(0, len(guess)):
            ans2 = guess[o]
            if (ans1 == ans2 or ans1.upper() == ans2.upper()) and p == o:
                blacks += 1

    for i in range(0, len(answer)):
        ans3 = answer[i]
        for j in range(0, len(guess)):
            ans4 = guess[j]
            if ((ans3 == ans4) or (ans3.lower() == ans4.lower())) and answer.index(ans3) != guess.index(ans4):
                whites += 1

    for a in range(0, len(guess)): # TESTING

        lowercasecol = []
        for t in range(len(colours)):
            newcol = colours[t]
            lowercasecol.append(newcol.lower())

        for u in range(len(guess)):
            col1 = guess[u]
            cond1 = False
            if col1.lower() not in lowercasecol:
                cond1 = True
                break

        for b in range(0, len(guess)):
            cond2 = False
            colcount = guess.count(guess[b])
            if colcount > 1:
                cond2 = True
                break
        
        if cond1 == True and cond2 == True:
            print('Sorry', name, ", the code maker cannot recognize the colour's you've entered. Additionally, repeats are not allowed. You've been given a penalty.")
            penalties += 1
            print('Toal penalties:', penalties)
            break

        if cond1:
            print('Sorry', name,",The code maker cannot recognize the colours you've entered. You've been given a penalty")
            penalties += 1
            print('Total penalties:', penalties)
            break
        
        if cond2:
            repeating = True
            print('Sorry', name, "repeated colours are not allowed in this game. You've been given a penalty")
            penalties += 1
            print('Total penalties:', penalties)
            break

    if sum == 15 and gameWon == False: # switch to shut off game; player has had too many guesses.
        gameOver = True
        break
    
    if penalties == 5:
        penalized = True
        break

    if blacks == 4:
        gameWon = True
        break
    if blacks == 1:
        print('You have', blacks,'black', end = ' ')
        if whites == 1:
            print('and', whites,'white,', end = ' ')
        elif whites > 1:
            print('and', whites,'whites,', end = ' ')
    
    if blacks > 1 or blacks < 0:
        print('You have', blacks,'blacks', end = ' ')
        if whites == 1:
            print('and', whites,'white,', end = ' ')
        elif whites > 1 or whites < 0:
            print('and', whites,'whites,', end = ' ')
    
    
    if blacks == 0:
        if whites == 1:
            print('you have', whites,'white,', end = ' ')
        elif whites > 1:
            print('you have', whites,'whites,', end = ' ')
    print(str(name), end ='.')
    print('\n')

    if blacks == 4:
        gameWon == True
        print('\n')
        break

if penalized:
    print(name,'you lost the game by reaching the maximum number of penalties. Sorry!')
    quit()

if gameOver:
    print('Sorry', name, ', you have ran out of guesses and have lost the game with', penalties,'penalties.')
    quit()
if gameWon:
    if sum == 1:
        print("You've won the game with", sum,'guess and', penalties, 'penalties!','Congratulations!' )
    elif sum > 1:
        print('You have won the game with', sum,'guesses and', penalties,'penalties!','Congratulations!')
        quit()
    
    