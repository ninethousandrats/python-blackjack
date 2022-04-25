"""
__init__(self)
draw_card(self, quantity)
"""

from Deck import Deck

class Player:
    def __init__(self):
        self.deck = Deck()
        self.hand = []
        self.handSize = 0
        
    def draw_card(self, quantity):
        for i in range(quantity):
            self.hand.append(self.deck.deal_card())
            print("added to hand: ", self.hand[i].suit, self.hand[i].rank)
            
#        self.deck.list_cards()