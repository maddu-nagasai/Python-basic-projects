import random

def get_computer_choice():
    """Randomly selects Rock, Paper, or Scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    """Determines the winner based on the game rules."""
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win! 🎉"
    else:
        return "Computer wins! 😢"

def main():
    print("\n✊📄✂️ Welcome to Rock, Paper, Scissors! ✊📄✂️")

    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("\nEnter rock, paper, or scissors (or 'quit' to stop): ").strip().lower()
        
        if player_choice == "quit":
            print(f"\nFinal Score - You: {player_score} | Computer: {computer_score}")
            print("Thanks for playing! Goodbye! 👋")
            break
        
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        if "win" in result:
            player_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        
        print(f"Score - You: {player_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()
