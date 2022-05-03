"""
__init__(self)
draw_card(self, newCard)
discard_card(self, index)
get_hand_value(self)
show_hand(self)
"""

from Card import Card

class Player:
    def __init__(self):
        self.hand = []
        self.handValue = 0
        
    def draw_card(self, newCard):
        self.hand.insert(0, newCard)
        
    def discard_card(self, index):
        return 0
    
    def get_hand_value(self):
        for x in range(len(self.hand)):
            self.handValue += self.hand[x].value
        return self.handValue
        
    def show_hand(self):
        for x in range(len(self.hand)):
            print(self.hand[x].suit, self.hand[x].rank)
            pass
