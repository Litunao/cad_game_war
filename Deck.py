import random
from Card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)
    
    def deal_half(self):
        """Splits the deck into two equal halves"""
        return self.cards[:26], self.cards[26:]