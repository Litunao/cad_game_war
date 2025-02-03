class Player:
    def __init__(self, name, cards):
        self.name = name
        self.deck = cards  # List of Card objects

    def play_card(self):
        return self.deck.pop(0) if self.deck else None  # Draw the top card
    
    def add_cards(self, won_cards):
        self.deck.extend(won_cards)  # Add cards to the bottom of the deck
    
    def has_cards(self):
        return len(self.deck) > 0