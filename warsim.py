import random as rd


# deck defs
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace",]

# creating the deck
deck = []
for card in cards:
    for i in range(4): # one for each suit
        deck.append(card)

# func to find the higher card
def return_winner(card_1:str, card_2:str, two_beats_ace:bool=True) -> int:
    card_1_val = cards.index(card_1)
    card_2_val = cards.index(card_2)
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

# splitting into two decks
def make_two_decks() -> tuple:
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
    return (deck_1, deck_2)

# simulate func
def simulate(two_beats_ace:bool=True, max_its:int=10000, verbose:bool=True, print_whole_deck:bool=False) -> None:
    deck_1, deck_2 = make_two_decks()
    iterations = 0
    while len(deck_1) > 0 and len(deck_2) > 0 and iterations <= max_its:
        if verbose:
            print("Iteration:", iterations)
            if print_whole_deck:
                print("Player 1 deck:", deck_1)
                print("Player 2 deck:", deck_2)
            print("Player 1 card:", deck_1[0])
            print("Player 2 card:", deck_2[0])

        # find the winning player and move the appropriate cards
        war_winnings = []
        while 1:
            winner = return_winner(deck_1[0], deck_2[0])
            if winner == 1:
                if verbose:
                    print("Player 1 won")
                deck_1.append(deck_2.pop(0))
                deck_1.append(deck_1.pop(0))
                if len(war_winnings) > 0:
                    deck_1 += war_winnings
                break
            elif winner == 2:
                if verbose:
                    print("Player 2 won")
                deck_2.append(deck_1.pop(0))
                deck_2.append(deck_2.pop(0))
                if len(war_winnings) > 0:
                    deck_2 += war_winnings
                break
            elif winner == 0: # init a war
                war_winnings += deck_1[0:3] + deck_2[0:3]
                del deck_1[0:3], deck_2[0:3]
                if verbose:
                    print("WAR Initiated")
                    print("Winnings at stake:", war_winnings)

        iterations += 1

if __name__ == "__main__":
    simulate()
