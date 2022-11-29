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


T1 = TexasHoldEm(4)
T1.add_card(3)
for b in range(0, 5):
    T1.add_to_table()

T1.print_hand(3)
T1.print_table()
T1.print_deck()

