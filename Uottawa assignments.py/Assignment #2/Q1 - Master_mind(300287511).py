#############################################################
#Anthony Le; 300287511
#Assignment 2, Question 21
# November 9, 2022

#############################################################
import random
colours = ['Red', 'Yellow', 'Blue', 'Green', 'Orange', 'Pink', 'Purple', 'Cyan', 'Silver', 'Teal']


penalties = 0


def randcol(x):
    answer = []
    i = 0
    numbers = []
    while i != 4: # MAKE INTO METHOD LATER . FOR [colours]
        y = random.randint(0, len(x) - 1)
        if y not in numbers:
            numbers.append(y)
            i += 1

    for j in range(0, len(numbers)):
        l = numbers[j]
        col = x[l]
        answer.append(col)

    return answer 

gameanswers = randcol(colours)
def blackCounter(x,y): #x,y = gameanswer, guess - gameanswers, ...
    blacks = 0
    for p in range(0, len(x)): # MAKE INTO METHOD LATER
        ans1 = x[p]
        for o in range(0, len(y)):
            ans2 = y[o]
            if (ans1 == ans2 or ans1.upper() == ans2.upper()) and p == o:
                blacks += 1

    return blacks

def whiteCounter(x,y): #x,y = gameanswers, guess...
    whites = 0
    for i in range(0, len(x)):
        ans3 = x[i]
        for j in range(0, len(y)):
            ans4 = y[j]
            if ((ans3 == ans4) or (ans3.lower() == ans4.lower())) and x.index(ans3) != y.index(ans4):
                whites += 1
    return whites

def condition1(x,y): #x,y = colours, guess
    for a in range(0, len(y)): # TESTING            
        lowercasecol = []
        for t in range(len(x)):
            newcol = x[t]
            lowercasecol.append(newcol.lower())

        for u in range(len(y)):
            col1 = y[u]
            cond1 = False
            if col1.lower() not in lowercasecol:
                cond1 = True
                break
    
    return cond1 

def condition2(x,y):
    for a in range(0, len(y)):
        cond2 = False
        colcount = y.count(y[a])
        if colcount > 1:
            cond2 = True
            break
    
    return cond2

def whiteblackCount(x,y,w): #x,y = blacks, whites, name
    gameWon = False
    if x == 1:
        if y == 1:
            return print(str(w) + ',','You have', x,'black and', y,'white.')
        elif y > 1 or y < 0:
            return print(str(w) + ',','You have', x,'black and', whites,'whites.')
    
    if x > 1 or x < 0:
        if y == 1:
            return print(str(w) + ',','You have', blacks,'blacks and', whites,'white.')
        elif y > 1 or y < 0:
            return print(str(w) + ',','You have', blacks,'blacks and', whites,'whites.')
    
    if x > 1 or x < 0:
        return print(str(w) +',', 'You have', blacks,'blacks')

    if x == 0:
        if y == 1:
            return print(str(w) + ',', 'you have', whites,'white.')
        elif y > 1:
            return print(str(w) + ',','you have', whites,'whites.')
    
        

def penaltycheck(x,y,w): # x,y,w = conditiondetermine1, conditiondetermine2, name
    
    if x == True and y == True:
        return (print('Sorry', w, ", the code maker cannot recognize the colour's you've entered. Additionally, repeats are not allowed. You've been given a penalty."))
    
    if x:
        return (print('Sorry', w,",The code maker cannot recognize the colours you've entered. You've been given a penalty,"))
        
    if y:
        return (print('Sorry', w, "repeated colours are not allowed in this game. You've been given a penalty."))
    

def output(blacks, sum, penalties, name): #x,y,z: blacks, sum, penalties, name 
    if sum == 15: # switch to shut off game; player has had too many guesses.
        return print('Sorry', name, ', you have ran out of guesses and have lost the game with', penalties,'penalties.')

    if penalties == 5:
        return print(name,'you lost the game by reaching the maximum number of penalties. Sorry!')
    
    if blacks == 4:
        if sum == 1:
            if penalties == 1:
                return print("You've won the game with", sum,'guess and', penalties, 'penalty!','Congratulations!' )
                
        if sum == 1:
            if penalties > 1 or penalties <= 0:
                return print("You've won the game with", sum,'guess and', penalties, 'penalties!','Congratulations!' )
        if sum > 1:
            if penalties == 1:
                return print('You have won the game with', sum,'guesses and', penalties,'penalty!','Congratulations!')
            elif penalties > 1 or penalties <= 0:
                return print('You have won the game with', sum,'guesses and', penalties,'penalties!','Congratulations!')

def outputTrigger(blacks,sum, penalties):
    if sum == 15:
        return quit()

    if penalties == 5:
        return quit()
    
    if blacks == 4:
        if sum == 1:
            if penalties == 1:
                return quit()
        if sum == 1:
            if penalties > 1 or penalties <= 0:
                return quit()
        elif sum > 1:
            if penalties == 1:
                return quit()
            elif penalties > 1 or penalties <= 0:
                return quit()

print('colours for game: ', gameanswers) #JUST FOR DEBUGGING.
name = str(input('What is your name?: '))
print('\n','Welcome to Master-Mind,', name,'!!')
print('The code maker is here. The available colours are:')
print('\n', ', '.join(colours))
print('\n', 'You have a total of 15 guesses and a total of 5 penalties are allowed. Try to avoid these penalties.')
print('The code maker has chosen four colours. You may now begin guessing,', name)
gameWon = False
gameOver = False

for n in range(0, 16):
    cond1 = False
    cond2 = False
    gameWon = False
    gameOver = False
    print('')
    print('Enter guess no.', n + 1, ': ', end = '')
    guess = list(map(str, input('').split()))
    print(guess)
    penalized = False
    sum = n + 1

    whites = whiteCounter(gameanswers, guess)
    blacks = blackCounter(gameanswers, guess) 

    conditionDetermine1 = condition1(colours, guess)
    conditionDetermine2 = condition2(colours, guess)
    
    if conditionDetermine1 == True or conditionDetermine2 == True or (conditionDetermine1 == True and conditionDetermine2 == True):
        penalties += 1

    penaltyfind = penaltycheck(conditionDetermine1,conditionDetermine2,name)
    whiteblacknum = whiteblackCount(blacks, whites, name)
    print('Total penalties:', penalties)

    decider = output(blacks, sum, penalties, name)

    decideTrigger = outputTrigger(blacks,sum, penalties)




    
    
    
    