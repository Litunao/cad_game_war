class Player:
    def __init__(self, name, cards):
        self.name = name
        self.deck = cards  # List of Card objects

    def play_card(self):
        """Plays the top card from the player's deck"""
        return self.deck.pop(0) if self.deck else None  

    def add_cards(self, won_cards):
        """Adds won cards to the bottom of the deck"""
        self.deck.extend(won_cards)  

    def has_cards(self):
        """Checks if the player still has cards left"""
        return len(self.deck) > 0