from Deck import Deck
from Player import Player

deck = Deck()
dealer = Player()
player = Player()

deck.shuffle()

gameIsRunning = True

while gameIsRunning:
    player.placeBet(input("How much would you like to bet? $"))
    
    # setup the round
    for x in range (2):
        player.draw_card(deck.deal_card())
        dealer.draw_card(deck.deal_card())
    
    dealer.show_hand(False)
    player.show_hand()
    
    # get player decision
    
    decision = "0"
    
    while decision != "2" and decision != "5":
        decision = input("1) Hit     2) Stand     3) Double Down\n4) Split   5) Surrender 6) Exit Game\n\nSelect Option: ")
        
        if decision == "1": player.draw_card(deck.deal_card())
        elif decision == "2": print("STANDING")
        elif decision == "3": player.doubleDown(deck.deal_card())
        elif decision == "4": player.split()
        elif decision == "5": player.surrender()
        elif decision == "6": print("Exit Function Goes Here")
        else: print("Invalid input, please try again.")

    break
