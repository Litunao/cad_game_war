import Player
import Deck

class WarGame:
    def __init__(self, player1_name="Player 1", player2_name="Player 2"):
        deck = Deck()
        half1, half2 = deck.deal_half()
        self.player1 = Player(player1_name, half1)
        self.player2 = Player(player2_name, half2)
        self.rounds_played = 0

    def play_round(self):
        """Plays a single round of War and returns the winner or None if ongoing."""
        self.rounds_played += 1
        print(f"\n--- Round {self.rounds_played} ---")

        if not self.player1.has_cards() or not self.player2.has_cards():
            return None  # Stop if a player has no cards
        
        card1 = self.player1.play_card()
        card2 = self.player2.play_card()
        print(f"{self.player1.name} plays {card1}")
        print(f"{self.player2.name} plays {card2}")

        table_cards = [card1, card2]

        while card1.value == card2.value:  # WAR condition
            print("WAR!")
            if len(self.player1.deck) < 4 or len(self.player2.deck) < 4:
                print("Not enough cards for WAR! Game ends.")
                return None

            war_cards1 = [self.player1.play_card() for _ in range(4)]
            war_cards2 = [self.player2.play_card() for _ in range(4)]
            table_cards.extend(war_cards1 + war_cards2)
            card1, card2 = war_cards1[-1], war_cards2[-1]  # Last card decides the war
            print(f"{self.player1.name} plays {card1} in WAR")
            print(f"{self.player2.name} plays {card2} in WAR")

        if card1.value > card2.value:
            self.player1.add_cards(table_cards)
            print(f"{self.player1.name} wins this round!")
        else:
            self.player2.add_cards(table_cards)
            print(f"{self.player2.name} wins this round!")

        return self.get_winner()

    def get_winner(self):
        """Returns the winner if the game is over, else None."""
        if len(self.player1.deck) == 52:
            return self.player1.name
        elif len(self.player2.deck) == 52:
            return self.player2.name
        return None