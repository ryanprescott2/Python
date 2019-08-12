# Python - PlayingCards.py File - 11 August 2019
# Author - John Ryan Prescott - johnryanprescott@gmail.com

import random


class Card:
    """ Card Class represents a playing card entity with value and suit"""

    suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    number_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    def __init__(self, value, suit):
        self.suit = self.suits[suit]  # assigning suit to card
        self.value = self.values[value]  # assigning value to card
        self.number_value = self.number_values[value]

    def __str__(self):
        return self.value + " of " + self.suit


class Deck:
    """ Deck class represents a set of all 52 standard playing cards"""

    def __init__(self):
        self.cards = []  # the decks list of cards
        self.cards = [Card(x, y) for x in range(13) for y in range(4)]  # creating the 52 card deck

    def remove_card(self, card):
        """ removes card of specified suit and value from the deck """
        for c in self.cards:
            if c == card:
                self.cards.remove(c)

    def generate_card(self):
        """ selects random card from deck """
        return random.choice(self.cards)

    def show_entire_deck(self):
        for i in self.cards:
            print(i)
