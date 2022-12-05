
def IsStraightFlush(list): # suit would be the same, but order of cards would be in increasing order or would have cards in increasing order.
    
    IsStraight = False
    numList = []
    for a in range(0, len(list)):
        val1 = list[a][0]
        numList.append(val1) # appends all values in order to set them and make sure they are in ascending order in increments of one

        sortedList = sorted(numList)
        straight = 0
        for b in range(1, len(numList)):
            if sortedList[b] == sortedList[b - 1] + 1:
                straight += 1
                
        print('Straight:',straight)
        if straight == 4:
            IsStraight = True
            print(IsStraight)
    IsFlush = False
    Dcount = 0
    Hcount = 0
    Acount = 0
    Scount = 0
    for a in range(0, len(list)):
        suit1 = list[a][1] # calls for suit of first card.
        if suit1 == 'H':
            Hcount += 1
        elif suit1 == 'D':
            Dcount += 1
        elif suit1 == 'A':
            Acount += 1
        elif suit1 == 'S':
            Scount += 1
        
    print('Dcount:', Dcount)
    if Dcount == 5 or Hcount == 5 or Acount == 5 or Scount == 5:
        IsFlush = True
        print('IsFlush:', IsFlush)

    if IsStraight == True and IsFlush == True:
        return True
    else:
        return False

def IsFourOfaKind(list): # four cards with the same rank;
    vals = []
    for a in range(0, len(list)):
        val1 = list[a][0]
        vals.append(val1)
    
    print(vals)

    for b in range(0, len(vals)):
        if vals.count(vals[b]) == 4:
            return True
    
    return False
            
        
def IsFlush(list): # all five cards have the same suit. 
        Dcount = 0
        Hcount = 0
        Acount = 0
        Scount = 0
        for a in range(0, len(list)):
            suit1 = list[a][1] # calls for suit of first card.
            if suit1 == 'H':
                Hcount += 1
            elif suit1 == 'D':
                Dcount += 1
            elif suit1 == 'A':
                Acount += 1
            elif suit1 == 'S':
                Scount += 1
        
        if Dcount == 5 or Hcount == 5 or Acount == 5 or Scount == 5:
            return True
        else:
            return False


def IsThreeOfaKind(list):
    vals = []
    for a in range(0, len(list)):
        val1 = list[a][0]
        vals.append(val1)
    
    print(vals)

    for b in range(0, len(vals)):
        if vals.count(vals[b]) == 3:
            return True
    
    return False

    
def IsFullHouse(list):
        Dcount = 0
        Hcount = 0
        Acount = 0
        Scount = 0
        for a in range(0, len(list)):
            suit1 = list[a][1] # calls for suit of first card.
            if suit1 == 'H':
                Hcount += 1
            elif suit1 == 'D':
                Dcount += 1
            elif suit1 == 'A':
                Acount += 1
            elif suit1 == 'S':
                Scount += 1
        
        if Dcount == 3 or Hcount == 3 or Acount == 3 or Scount == 3:
            if Dcount == 2 or Hcount == 2 or Scount == 2 or Acount == 2:
                return True
            else:
                return False

        #use tempList for other check. if the cards with the same suit are removed, the others should be left in the tempList.
            
        
def IsStraight(list): # when all five cards ranks are in ascending order; list may not be in ascending order itself though. 
        numList = []
        for a in range(0, len(list)):
            val1 = list[a][0]
            numList.append(val1) # appends all values in order to set them and make sure they are in ascending order in increments of one

        sortedList = sorted(numList)
        print(sortedList)

        straight = 0
        for b in range(1, len(numList)):
            if sortedList[b] == sortedList[b - 1] + 1:
                straight += 1
                print(straight)
        
        if straight == 4:
            return True
        else:
            return False
    
def IsTwoPairs(list): # find four cards; two cards have the same rank, no care for suit
    valList = []
    for a in range(len(list)):
        val = list[a][0]
        valList.append(val)
    print(valList)
    
    pairs = 0
    plusValues = []
    for a in range(len(valList)):
        num = valList[a]
        if num not in plusValues:
            if valList.count(num) == 2:
                pairs += 1
            plusValues.append(num)
        
        if pairs == 2:
            return True
    
    return False

def IsOnePair(list):
    values = []
    for a in range(0, len(list)):
        val1 = list[a][0]
        values.append(val1)
    
    for b in range(0, len(values)):
        if values.count(values[b]) == 2:
            return True
        
    return False

# suit would be the same, but order of cards would be in increasing order or would have cards in increasing order.

T1 = [[6, 'D'], [7, 'D'], [8, 'D'], [9, 'D'], [10, 'D']]

if IsStraightFlush(T1):
    print('True')
else:
    print('False')

if IsStraight(T1):
    print('True')
else:
    print('False')


