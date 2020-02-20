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


print("Welcome to war!")

# Logic

d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

computer_player = Player("computer", Hand(half1))

name = input("What is your name")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and computer_player.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("Current standings")
    print(user.name + "has the count: "+ str(len(user.hand.cards)))
    print(computer_player.name + "has the count: " + str(len(computer_player.hand.cards)))
    print("Play a card")
    print('\n')

    table_cards = []

    c_card = computer_player.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1
        print("War")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(computer_player.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            computer_player.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            computer_player.hand.add(table_cards)

print("Game over, number of rounds: " + str(total_rounds))
print("A war happened " + str(war_count) + " times")
















