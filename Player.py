"""
__init__(self)
draw_card(self, quantity)
discard_card(self, index)
show_hand(self)
"""

from Deck import Deck

class Player:
    def __init__(self):
        self.deck = Deck()
        self.hand = []
        self.handSize = 0
        
    def draw_card(self, quantity):
        print("Added to Hand:")
        for i in range(quantity):
            self.hand.append(self.deck.deal_card())
            self.handSize += 1
            print(self.hand[i].suit, self.hand[i].rank)
            
    def discard_card(self, index):
        # pass a card to self.deck
        self.deck.add_to_discard(self.hand[index])
        self.handSize -= 1
        
    def show_hand(self):
        for x in range(self.handSize):
            #print(self.hand[x].value)
            print(self.hand[x].suit, self.hand[x].rank)
            
#        self.deck.list_cards()
        self.deck.list_discardedCards()