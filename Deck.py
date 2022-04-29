"""
__init__(self)
list_cards(self) #remove later
list_discardedCards(self) #remove later
deal_card(self)
add_to_discard(self, tempCard)
shuffle_deck(self)
"""

from Card import Card
import random
        
class Deck:    
    def __init__(self):
        self.cards = []
        self.discardedCards = []

        for s in ["♠","♥","♦","♣"]:
            for r in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
                self.cards.append(Card(s,r,len(self.cards)))
                
    #debug method
    def list_cards(self):
        for x in range(len(self.cards)):
            #print(self.cards[x].value)
            print(self.cards[x].suit, self.cards[x].rank)
            
    #debug method
    def list_discardedCards(self):
        print("Discard Pile:")
        for x in range(len(self.discardedCards)):
            #print(self.discardedCards[x].value)
            print(self.discardedCards[x].suit, self.discardedCards[x].rank)
            
    def deal_card(self):
        tempCard = self.cards[0]
        self.cards.pop(0)
        return tempCard
    
    def add_to_discard(self, tempCard):
        self.discardedCards.insert(0, tempCard)
    
    def shuffle_deck(self):
        random.shuffle(self.cards)
