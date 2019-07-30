from random import randint

def build_deck(deck,suits,values):
    """Build a full deck of cards"""
    for suit in suits:
        for value in values:
            card = str(value) + "|" +str(suit)
            deck.append(card)
    return(deck)
            
def show_deck(deck):
    """Shows the full deck"""
    print("This is the current deck:\n")
    print(str(deck) + "\n")
    
def shuffle_deck(deck):
    """Shuffle a deck"""
    shuffled_deck = []
    while len(deck) > 1:
        shuffled_deck.append(deck.pop(randint(0,(len(deck)-1))))
    return(shuffled_deck)
