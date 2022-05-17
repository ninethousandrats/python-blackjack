"""
__init__(self)
draw_card(self, newCard)
discard_card(self, index)
get_hand_value(self)
show_hand(self)

doubleDown(self)
split(self)
surrender(self)
winBet(self)
"""

from Card import Card

class Player:
    def __init__(self):
        self.hand = []
        self.handValue = 0
        self.handBet = 0
        self.chips = 50000
        
    def draw_card(self, newCard):
        self.hand.insert(0, newCard)
        
    def discard_card(self, index):
        return 0
    
    def get_hand_value(self):
        for x in range(len(self.hand)):
            self.handValue += self.hand[x].value
        return self.handValue
        
    def show_hand(self, allCards = True):
        if allCards:
            for x in range(len(self.hand)):
                print(self.hand[x].suit, self.hand[x].rank)
        else:
            print(self.hand[0].suit, self.hand[0].rank)
            print("▯","▯")
        
        print(" ")
            
    def placeBet(self, bet):
        if int(bet) <= self.chips:
            self.chips -= int(bet)
            self.handBet= int(bet)
    
    def doubleDown(self, newCard):
        if self.handBet >= self.chips:
            self.chips - self.handBet
            self.handBet = self.handBet * 2
        self.hand.insert(0, newCard)
        print("double or nothin")
        
    def split(self):
        print("cut my hand into pieces")
        
    def surrender(self):
        self.chips += self.handBet / 2
        print("half bet")
        
    def winBet(self):
        self.chips += self.handBet
        print("You won the hand!")
        
        
