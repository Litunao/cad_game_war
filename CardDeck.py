import random
from WAR_game import Card

class card_deck:
    def __init__(self):
        self.rank = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.suit = ['Hearts','Diamonds','Clubs','Spades']
        self.values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7','8','9','10','J','Q','K','A'}
        self.deck = []
        for i in self.suit:
            for j in self.rank:
                self.deck.append(Card(j,i))
        random.shuffle(self.deck)

    def deal(self):
        if len(self.) > 0:
            return self.hand.pop(0)
        else:
            return None