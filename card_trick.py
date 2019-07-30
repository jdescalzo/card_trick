from deck import *

deck = []
suits = ['♠','♥','♦','♣']
values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = shuffle_deck(build_deck(deck,suits,values))[:21]

deck_top = []
deck_middle = []
deck_bottom = []

def deck_cut():
    """Separate the deck in three parts"""
    while len(deck) > 0:
        for card in deck:
            current_card = deck.pop()
            if len(deck) % 3 == 0:
                deck_top.append(current_card)
            elif len(deck) % 3 == 2:
                deck_middle.append(current_card)
            elif len(deck) % 3 == 1:
                deck_bottom.append(current_card)
    
def show_decks():
    """Shows the three piles"""
    print("1: " + str(deck_top))
    print("2: " + str(deck_middle))
    print("3: " + str(deck_bottom))
    
def deck_build(middle,top,bottom):
    """Makes a full deck from the three piles"""
    while len(top)>0:
        for card in top:
            current_card = top.pop(0)
            deck.append(current_card)
    while len(middle)>0:
        for card in middle:
            current_card = middle.pop(0)
            deck.append(current_card)
    while len(bottom)>0:
        for card in bottom:
            current_card = bottom.pop(0)
            deck.append(current_card)

def deck_rebuild(choice):
    """Set the order of the piles in the new deck"""
    if choice == 1:
        deck_build(deck_top,deck_middle,deck_bottom)
    elif choice == 2:
        deck_build(deck_middle,deck_top,deck_bottom)
    elif choice == 3:
        deck_build(deck_bottom,deck_middle,deck_top)

while True:

    deck_cut()

    print("Welcome to this magic trick! Please follow the instructions")
    print("Enter 'quit' any time to stop playing")
    print("Pick a card from any of the three decks below:\n")

    show_decks()

    choice = input("\nWas your card in the deck '1', '2' or '3'? ")
    if choice == 'quit':
        break
    else: 
        deck_rebuild(int(choice))
        deck_cut()

    print("\nGreat! Now, once again.\n")

    show_decks()

    choice = input("\nIs your card in deck '1', '2' or '3'? ")
    if choice == 'quit':
        break
    else:
        deck_rebuild(int(choice))
        deck_cut()

    print("\nPerfect! One last time!\n")

    show_decks()

    choice = input("\nIs your card in deck '1', '2' or '3'? ")
    if choice == 'quit':
        break
    else:
        deck_rebuild(int(choice))

    print("\n\tYour card is: " + str(deck[10]) + "!\n")
    
    cont = input("Do you want to play again? (y/n) ")
    if cont == 'n':
        break
    else:
        print('\n ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ \n')
