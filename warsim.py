import random as rd


# deck defs
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace",]
suits = ["hearts", "diamonds", "spades", "clubs"]

# creating the deck
deck = []
for card in cards:
    for suit in suits:
        deck.append([card, suit])

# func to find the higher card
def return_winner(card_1:list, card_2:list, two_beats_ace:bool=True) -> int:
    card_1_val = cards.index(card_1[0])
    card_2_val = cards.index(card_2[0])
    if two_beats_ace and ((card_1_val == 0 and card_2_val == 51) or (card_1_val == 51 and card_2_val == 0)):
        if card_1_val == 0:
            return 1
        elif card_2_val == 0:
            return 2
    else:
        if card_1_val > card_2_val:
            return 1
        elif card_2_val > card_1_val:
            return 2
        elif card_1_val == card_2_val:
            return 0
    return 0

#splitting into two decks
deck_1 = []
deck_2 = []
remaining_indices = list(range(len(deck)))
while len(remaining_indices) > 0:
    for i in range(2):
        index_choice = rd.choice(remaining_indices)
        remaining_indices.remove(index_choice)

        if i == 0:
            deck_1.append(deck[index_choice])
        elif i == 1:
            deck_2.append(deck[index_choice])

def simulate(two_beats_ace:bool=True) -> None:
    # complete the simulate func
    print("simulate")
    pass

if __name__ == "__main__":
    simulate()
