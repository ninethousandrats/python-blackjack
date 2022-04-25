"""
__init__(self)
list_cards(self) #remove later
deal_card(self)
shuffle_deck(self)
"""

from Card import Card
import random
        
class Deck:    
    def __init__(self):
        self.cards = []
        self.deckSize = 0

        self.discardedCards = []
        self.discardSize = 0

        print("Creating Deck!")        
        
        for s in ["♠","♥","♦","♣"]:
            for r in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
                self.deckSize += 1
                self.cards.append(Card(s,r,self.deckSize))
    
    #debug method
    def list_cards(self):
        for x in range(self.deckSize):
            #print(self.cards[x].value)
            print(self.cards[x].suit, self.cards[x].rank)
            
    def deal_card(self):
        tempCard = []
        tempCard.append(self.cards[0])
        self.cards.pop(0)
        self.deckSize -= 1
        return tempCard[0]
    
    def shuffle_deck(self):
        random.shuffle(self.cards)
        
        
        
        
        
        
        
        
        