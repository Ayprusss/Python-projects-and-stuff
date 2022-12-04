import random

class TexasHoldEm:

    def __init__(self, players = 2):
        rank = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K']
        suit = ['D', 'C', 'S', 'H']
        self.players = players # initializes number of players within the game
        tableHands = [] # all players' hands that are present on the table.
        
        for i in range(0, players):
            playerhand = []
            tableHands.append(playerhand) #appends an empty list to the tableHands list; represents the player's hand and how many players are on the table. 
        self.playerHands = tableHands

        deck = []
        x = 0
        while x != 52: #52 cards in a single deck.
            card = [] #to find the one card to be put into the deck
            card.append(rank[random.randint(0, len(rank) - 1)]) #picks out a random rank for the card
            card.append(suit[random.randint(0, len(suit) - 1)]) # picks out a random suit for the card
            if card not in deck: # checks if card is not in the deck; it's unique.
                deck.append(card) # puts the card into the deck
                x += 1 # upped the count of how many cards are in the deck.
        print(deck)

        self.deck = deck
        table = [] # table is the table in which cards are to be presented for players to get best combination.
        self.table = table 
    
    def add_card(self,index): # function is asking for player with the index to have the card on top of the deck be added to the player's hand. Need to create a deck before doing this.
        #adding a card into someone's hand would also remove a card from the deck list. Len must change as well as the deck itself. 
        decklist= self.deck
        card = decklist[0]
        self.playerHands[index - 1].append(card)
        self.deck.remove(card)
        #print('deck now:', self.deck)
        '''for j in range(0, players):
            playerhand = []
            for i in range(0, 5): # five cards put into the player's hands
                card = []
                rankval = random.randint(0, len(rank) - 1)
                suitval = random.randint(0, len(suit) - 1)
                card.append(rank[rankval])
                card.append(suit[suitval])
                playerhand.append(card)
            
            tableCards.append(playerhand)
        self.playerCards = tableCards
        # I DIDN'T NEED TO DO ALL OF THIS ;-; NEED TO INPUT AN EMPTY LIST FOR EACH PLAYER, NOT TO GIVE THEM CARDS AT ALL'''

    def print_hand(self, index): #DEBUGGING OPERATOR
        return print('Player', str(index)+ "'s", 'hand:', self.playerHands[index - 1])

    def add_to_table(self): # to add a card to the table
        decklist = self.deck #grabs the deck of cards with the remaining cards
        card = decklist[0] # picks out the first card of the deck
        self.table.append(card) #places the card onto the table
        self.deck.remove(card) # removes card from the deck. 

    def print_table(self):#DEBUGGING OPERATOR
        return print('table:', self.table)
    
    def print_deck(self):#DEBUGGING OPERATOR
        return print('deck:', self.deck)

    '''def IsStraightFlush(self, list): # suit would be the same, but order of cards would be in increasing order or would have cards in increasing order. 
        for a in range(1, len(list)): #list in this case would have length of 5.
            for b in range(0, 2):'''
    def IsStraightFlush(self, list): # suit would be the same, but order of cards would be in increasing order or would have cards in increasing order. 
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

    def IsFourOfaKind(self, list): # four cards with the same rank;
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
        
    def IsFlush(self, list): # all five cards have the same suit. 
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

    def IsThreeOfaKind(self, list):
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
            suit1count = 1
            for b in range(1, len(list)):
                nextSuit = list[b][1] # calls for suit of the second card; ISSUE; saying list index is out of range. #FIX
                print('next suit:', nextSuit) 
                if suit1 == nextSuit:
                    suit1count += 1
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
            
        
    def IsStraight(self, list): # when all five cards ranks are in ascending order; list may not be in ascending order itself thhough. 
        numList = []
        for a in range(0, len(list)):
            val1 = list[a][0]
            numList.append(val1) # appends all values in order to set them and make sure they are in ascending order in increments of one

        sortedList = sorted(numList)

        for b in range(1, len(numList)):
            if sortedList[b] == sortedList[b -1] + 1:
                return True
        
        return False
    
    def IsTwoPairs(self, list): # find four cards; two cards have the same rank, no care for suit
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

    def isOnePair(self, list):
        for a in range(0, len(list)):
            val1 = list[a][0]
            for b in range(1, len(list)):
                val2 = list[b][0]
                if val1 == val2: # one pair is found; nothing else. 
                    return True
        
        return False

T1 = TexasHoldEm(4)
T1.add_card(3)
for b in range(0, 5):
    T1.add_to_table()

T1.print_hand(3)
T1.print_table()
T1.print_deck()

