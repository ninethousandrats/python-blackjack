from Player import Player

player1 = Player()
player1.deck.shuffle_deck()
player1.draw_card(3)

player1.discard_card(0)
print("New Hand:")
player1.show_hand()

#player1.deck.list_cards()