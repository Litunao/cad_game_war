class Card:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.ranks.index(rank)  # Assign numerical value based on rank
    
    def __repr__(self):
        return f"{self.rank} of {self.suit}"