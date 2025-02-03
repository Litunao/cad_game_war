from WAR_game import WarGame

def play_game():
    game = WarGame("Alice", "Bob")

    print("Starting WAR Game!\n")
    while True:
        winner = game.play_round()
        if winner:
            print(f"{winner} wins the game!")
            break

    print("\nGame Over!")

if __name__ == "__main__":
    play_game()