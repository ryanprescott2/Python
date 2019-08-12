# Python - BlackJack.py File - 11 August 2019
# Author - John Ryan Prescott - johnryanprescott@gmail.com

# Text based black jack game with betting. Currently no double or split functionality

import PlayingCards
import People


from People import Player
dealer = People.Player("dealer")
player = People.Player("player")


def start_game():
    print("-------  Welcome to BlackJack  ---------")
    print("-------  You start with $3000  ---------")
    name = input("What is your name?\n")
    player.name = name
    del name
    print("Welcome, ", player.name)
    start_round()


def start_round():
    player.hand.clear()
    dealer.hand.clear()
    if player.balance <= 0:
        print("You are out of money! --- Goodbye!")
        exit()
    print("You currently have $ ", player.balance)
    game_deck = PlayingCards.Deck()
    wager(player)
    deal_cards(2, game_deck, player)
    check_jackpot(player)
    deal_cards(2, game_deck, dealer)
    check_jackpot(dealer)
    player_action = None
    dealer_action = None
    turn = 0
    while True:
        turn += 1
        print("*=*=*=*=* Turn  # {turn} *=*=*=*=*".format(turn=turn))
        if player_action == "hold" and dealer_action == "hold":
            round_over()
        elif player_action == "hold":
            dealer_action = dealer_turn(game_deck)
        else:
            player_action = player_turn(turn, game_deck)
            dealer_action = dealer_turn(game_deck)


def round_over():
    if player.get_hand_value() >= dealer.get_hand_value():
        player_won(win="normal")
    elif player.get_hand_value() < dealer.get_hand_value():
        player_lost(loss="beat by dealer")


def player_turn(turn, deck):
    if turn == 1:
        answer = input("Would you like to double your wager?\n")
        if answer in ["yes", "ye", "ya", "y", "double"]:
            if player.balance > player.current_wager:
                player.current_wager = player.current_wager * 2
                print("Now Betting $", player.current_wager)
            else:
                print("You do not have enough to double your money")
    action = input("Would you like to hold or hit?\n")
    while True:
        if action not in ["hold", "hit", "Hold", "Hit"]:
            print("Please type 'hold' or 'hit'")
            continue
        else:
            break
    if action in ["hold", "Hold"]:
        print("Holding cards")
        return "hold"
    if action in ["hit", "Hit"]:
        deal_cards(1, deck, player)
        check_bust(player)
        check_jackpot(player)
    return "hit"


def dealer_turn(deck):
    if dealer.get_hand_value() < 17:
        print("Dealer hits")
        deal_cards(1, deck, dealer)
        check_bust(dealer)
        check_jackpot(dealer)
        return "hit"
    else:
        print("Dealer holding cards")
        return "hold"


def player_lost(loss="beat by dealer"):
    if loss == "beat by dealer":
        print("The dealer beat you! - You lost ${wager} to the dealer".format(wager=player.current_wager))
        print("The dealer had ", dealer.get_hand_value())
    elif loss == "bust":
        print("You went over 21 - You lost ${wager} to the dealer".format(wager=player.current_wager))
    elif loss == "dealer got jackpot":
        print("Dealer got a BlackJack! - You lost ${wager} to the dealer".format(wager=player.current_wager))
    player.balance -= player.current_wager
    print("Starting new round...")
    start_round()


def player_won(win="normal"):
    earnings = 0
    if win == "jackpot":
        earnings = 1.5 * player.current_wager
        print("You got a BlackJack!")
    elif win == "normal":
        earnings = 1 * player.current_wager
        print("You beat the dealer!")
    elif win == "dealer bust":
        earnings = 1 * player.current_wager
        print("The dealer went over 21!")
    print("The dealer had ", dealer.get_hand_value())
    player.balance += earnings
    print("Your earnings are ${earn} and balance is ${balance}".format(earn=earnings, balance=player.balance))
    print("Starting new round...")
    start_round()


def check_bust(player):
    if player.get_hand_value() > 21:
        if player.name is "dealer":
            player_won(win="dealer bust")
        else:
            player_lost(loss="bust")


def check_jackpot(player):
    if player.get_hand_value() == 21:
        if player.name is "dealer":
            player_lost(loss="dealer got jackpot")
        else:
            player_won(win="jackpot")


def wager(player):
    global bet
    while True:
        try:
            bet = int(input("How much $ do you want to wager?\n"))
        except ValueError:
            print("Please type an integer")
            continue
        else:
            if bet > player.balance:
                print("You do not have enough, try a lower wager")
                continue
            elif bet <= 0:
                print("You must bet a positive amount of money")
                continue
            break
    player.current_wager = bet
    print("Betting $", bet)


def deal_cards(num_cards, deck, player):
    for i in range(num_cards):
        new_card = deck.generate_card()
        deck.remove_card(new_card)
        player.add_card_to_hand(new_card)
        if i >= 1 and player.name is "dealer":
            continue
        print("Dealt a {card} to {player}".format(card=new_card, player=player.name))


if __name__ == "__main__":
    start_game()

