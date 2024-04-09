## Poker

import random

class Card:
    SUITS = ['♠', '♣', '♦', '♥']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        if suit not in self.SUITS:
            raise Exception(f"Invalid suit. Must be one of {self.SUITS}")
        if rank not in self.RANKS:
            raise Exception(f"Invalid rank. Must be one of {self.RANKS}")
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit
    @property
    def rank(self):
        return self._rank

    # need to be able to print the card
    def __str__(self):
        return f"{self._rank}{self._suit}"
    def __repr__(self):
        return self.__str__()

class Deck:
    def __init__(self):
        cards = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                cards.append(Card(suit=suit, rank=rank))
        cards = tuple(cards)
        self._cards = cards

    def Shuffle(self):
        cards = list(self._cards)
        random.shuffle(cards)
        self._cards = tuple(cards)

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return self._cards

class PokerHand:
    def __init__(self, deck):
        hand = []
        for i in range(5):
            hand.append(deck.cards[i])
        self._hand = hand

    @property
    def cards(self):
        return self._hand

    def __str__(self):
        return self._hand

    @property
    def is_Flush(self):
        suit = self._hand[0].suit
        for card in self._hand:
            if card.suit != suit:
                return False
        return True

while True:
    deck = Deck()
    deck.Shuffle()
    hand = PokerHand(deck)
    if hand.is_Flush:
        print("Flush!")
        print(hand.cards)
        break




card = Card('♠', 'K')
print(card)
card2 = Card('♣', '4')
print(card2)

cards_list = [card, card2]
print(cards_list)

deck = Deck()
print(deck.cards)
deck.Shuffle()
print(deck.cards)

hand = PokerHand(deck)
print(hand.cards)