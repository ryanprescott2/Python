# Python - People.py File - 11 August 2019
# Author - John Ryan Prescott - johnryanprescott@gmail.com


class Player:
    current_wager = 0

    def __init__(self, name, balance=3000, hand=None):
        self.name = name
        self.balance = balance
        if hand is None:
            hand = []
        self.hand = hand

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        sum = 0
        for card in self.hand:
            sum += card.number_value
        return sum


    @property
    def hand_size(self):  # returns number of cards in Player's hand
        return len(self.hand)
