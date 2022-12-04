
def IsStraightFlush(list): # suit would be the same, but order of cards would be in increasing order or would have cards in increasing order. 
        sameSuit = True
        for a in range(0, len(list)): #list in this case would have length of 5.
            suit1 = list[a][1] # checks the suit of the first card to be compared with. [3, C] = C
            for b in range(1, len(list)):
                suit2 = list[b][1] # checks same thing for card ahead.
                if suit1 != suit2:
                    sameSuit = False
                    break
        
            if sameSuit == False: # one card does not have the same suit. 
                return False
    
        if sameSuit == True: # check if the numbers are going in an ascending order now. 
            ranklist = []
            for c in range(0, len(list)): # numbers might not be in ascending order; need to make it so it is.
                rank = list[c][0]
                ranklist.append(rank) # grab all ranks and put them into a list. ERROR: some might have the strings. 
        
            orderedrank = sorted(ranklist)
            for x in range(1, len(orderedrank)):
                if orderedrank[x] != orderedrank[x - 1] + 1:
                    return False
            
            return True

def IsFourOfaKind(list): # four cards with the same rank;
        for a in range(0, len(list)):
            val1 = list[a][0]
            sameval = 1
            for b in range(1, len(list)):
                val2 = list[b][0]
                if val1 == val2:
                    sameval += 1
            
            if sameval == 4:
                return True
        
        return False
        
def IsFlush(list): # all five cards have the same suit. 
        for a in range(0, len(list)):
            val1 = list[a][1]
            sameval = 1
            for b in range(1, len(list)):
                val2 = list[b][1]
                if val1 == val2:
                    sameval +=1 
                
            if sameval == 5:
                return True
            
        
        return False

def IsThreeOfaKind(list):
        for a in range(0, len(list)):
            val1 = list[a][0]
            sameval = 1
            for b in range(1, len(list)):
                val2 = list[b][0]
                if val1 == val2:
                    sameval += 1

            
            if sameval == 3:
                return True
    
        return False

    
def IsFullHouse(list):
        tempList = list
        for a in range(0, len(list) - 1):
            suit1 = list[a][1] # calls for suit of first card.
            print('suit:', suit1)
            suit1count = 1
            for b in range(1, len(list)):
                nextSuit = list[b][1] # calls for suit of the second card; ISSUE; saying list index is out of range. #FIX
                print('next suit:', nextSuit) 
                if suit1 == nextSuit:
                    suit1count += 1
                    print(suit1count)
                    tempList.remove(list[b])
                    tempList.remove(list[a])
                if suit1count <= 2 or suit1count >= 3:  # the two or three cards of one suit has been found. now to find the other three or two of another.
                    comb1 = True
                    break
            if comb1:
                break
            
        #use tempList for other check. if the cards with the same suit are removed, the others should be left in the tempList.

        for a in range(0, len(tempList)):
            suit2 = tempList[a][1]
            suit2count = 1
            for b in range(1, len(tempList)):
                nextSuit = tempList[b][1]
                if suit2 == nextSuit:
                    suit2count += 1
            
            if suit2count == 2 or suit2count == 3: #second set for the other suits equals to 2 or 3, means that it is a full house.
                return True
            else:
                return False
            
        
def IsStraight(list): # when all five cards ranks are in ascending order; list may not be in ascending order itself though. 
        numList = []
        for a in range(0, len(list)):
            val1 = list[a][0]
            numList.append(val1) # appends all values in order to set them and make sure they are in ascending order in increments of one

        sortedList = sorted(numList)

        for b in range(1, len(numList)):
            if sortedList[b] == sortedList[b -1] + 1:
                return True
        
        return False
    
def IsTwoPairs(list): # find four cards; two cards have the same rank, no care for suit
    valList = []
    for a in range(len(list)):
        val = list[a][0]
        valList.append(val)
    
    pairs = 0
    for a in range(len(valList)):
        num = valList[a]
        if valList.count(num) == 2:
            pairs += 1
    
    if (pairs // 2) ==2:
        return True
    else: 
        return False

def IsOnePair(list):
        for a in range(0, len(list)):
            val1 = list[a][0]
            for b in range(1, len(list)):
                val2 = list[b][0]
                if val1 == val2: # one pair is found; nothing else. 
                    return True
        
        return False


T1 = [[4, 'H'], [6, 'S'], [8, 'H'], [7, 'S'], [5, 'H']]


if IsFullHouse(T1):
    print('True')
else:
    print('False')

