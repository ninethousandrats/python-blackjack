from Deck import Deck
from Player import Player

deck = Deck()
player = Player()

deck.shuffle()

for x in range (2):
    player.draw_card(deck.deal_card())

player.show_hand()
print(player.get_hand_value())
