import random as rd


# deck defs
card_vals: list[str] = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace",]

# creating the deck
deck: list[str] = []
for card in card_vals:
    for i in range(4): # one for each suit
        deck.append(card)

# func to find the higher card
def return_winner(card_1:str, card_2:str, two_beats_ace:bool|int=True) -> int:
    """Give two strings from list `card_vals` and return higher card or tie as int in 1, 2, 0."""
    card_1_val = card_vals.index(card_1)
    card_2_val = card_vals.index(card_2)
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
def make_two_decks() -> tuple[list[str], list[str]]:
    """Create two random decks from a master deck (their sum being the provided deck)."""
    deck_1: list[str] = []
    deck_2: list[str] = []
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
def simulate(two_beats_ace:bool=True, max_its:int=10000, verbose:bool|int=True, print_winner:bool|int=True, print_whole_deck:bool|int=False) -> tuple[int, int, list, list]: # [winning player (1 or 2), iteration count, player_1_card_data, player_2_card_data]
    """Simulates a game of war between two players.

    Keyword Arguments:
        two_beats_ace -- boolean, whether or not a two will be considered higher than an ace (default True)
        max_its -- int, maximum simulation iteration (default 10000)
        verbose -- bool|int, wether the program will print certain extra information to the terminal, does not affect final winner output (default True)
        print_winner -- bool|int, wether the program will print the winner when verbose == False, or if verbose or print_winner then print (default True)
        print_whole_deck -- bool|int, whether the program will print the whole deck of either player each iteration when verbose == True (default False)

    Output:
        simulate() outputs a tuple with four indices.
        0: (type int) winning player as 1 or 2
        1: (type int) number of iterations
        2: (type list[int]) number of card_vals in player 1's deck at each iteration
        3: (type list[int]) number of card_vals in player 2's deck at each iteration
    """
    deck_1, deck_2 = make_two_decks()
    iterations = 0
    player_1_card_data, player_2_card_data = [], [] # for capturing data to plot

    # game loop
    while len(deck_1) > 0 and len(deck_2) > 0 and iterations <= max_its:
        # data collection
        player_1_card_data.append(len(deck_1))
        player_2_card_data.append(len(deck_2))

        # output
        if verbose:
            print("Iteration:", iterations)
            if print_whole_deck:
                print("Player 1 deck:", deck_1)
                print("Player 2 deck:", deck_2)
            print("Player 1 has", len(deck_1), "card_vals")
            print("Player 2 has", len(deck_2), "card_vals")
            print("Player 1 card:", deck_1[0])
            print("Player 2 card:", deck_2[0])

        # find the winning player and move the appropriate card_vals
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
                if verbose:
                    print("WAR Initiated")
                if len(deck_1) <= 3 or len(deck_2) <= 3: # if someone has insufficient card_vals, set to 0 to make them lose
                    if len(deck_1) <= 3:
                        deck_1 = []
                    elif len(deck_2) <= 3:
                        deck_2 = []
                    break
                war_winnings += deck_1[0:3] + deck_2[0:3]
                del deck_1[0:3], deck_2[0:3]
                if verbose:
                    print("Winnings at stake:", war_winnings)

        if verbose:
            print("\n")

        iterations += 1

    # declare winner
    winner = 0
    if len(deck_1) == 0:
        if verbose or print_winner:
            print("Player 2 won the game!")
        winner = 2
    elif len(deck_2) == 0:
        winner = 1
        if verbose or print_winner:
            print("Player 1 won the game!")

    # return values
    return winner, iterations, player_1_card_data, player_2_card_data
