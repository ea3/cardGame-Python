from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    def __init__(self):
        print("Creating new ordered deck")
        self.all_cards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.all_cards)

    def split_in_half(self):
        return self.all_cards[:26], self.all_cards[26:]


class Hand:

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_cards(self):
        return self.cards.pop()


class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_cards()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        for x in range(3):
            war_cards.append(self.hand.cards.pop())
        return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0












