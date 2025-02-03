# card_game_war
A card game called WAR, practice project.

# Game rules
The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals the top card of their deck—this is a "battle"—and the player with the higher card takes both of the cards played and moves them to their stack. Aces are high, and suits are ignored.

If the two cards played are of equal value, then there is a "war". Both players place the next card from their pile face down and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.

# WAR Card Game (Python Implementation)

## 📌 Overview
WAR is a simple card game for two players. Each player plays the top card from their deck, and the higher-ranked card wins. If there is a tie, a "WAR" occurs, where more cards are played.

## 📁 Project Structure
war_game/ │── Card.py # Defines the Card class │── Deck.py # Handles deck creation and shuffling │── Player.py # Manages player logic │── WAR_game.py # Implements the core game logic │── Main.py # Entry point for the game │── README.md # Instructions and details about the game

markdown
Copy
Edit

## ▶️ How to Run the Game
1. **Ensure you have Python installed** (version 3.x recommended).
2. Open a terminal and navigate to the project folder.
3. Run the game using:
   ```bash
   python Main.py
🎮 How to Play
The game runs automatically in rounds.
Each round, both players play a card.
If the cards are equal, a WAR occurs.
The game continues until one player has all the cards.
🔧 Future Improvements
Add GUI using Tkinter or Pygame.
Implement multiplayer mode.
Enjoy the game! 🎲
