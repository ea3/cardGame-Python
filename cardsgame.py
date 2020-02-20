SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        print("Creating new ordered deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]







        