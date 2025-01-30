import random

class card_deck:
    def __init__(self):
        self.rank = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.suit = ['Hearts','Diamonds','Clubs','Spades']
        self.deck = []
        for i in self.suit:
            for j in self.rank:
                self.deck.append(card(j,i))
        random.shuffle(self.deck)

def deal(self):
    if len(self.deck) > 0:
        return self.deck.pop(0)
    else:
        return None

class player:
    def __init__(self,name):
        self.name = name
        self.hand = []

def draw(self,deck):
    self.hand.append(deck.deal())




class card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit







