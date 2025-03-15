import random

def roll_dice(sides=6):
    """Simulates rolling a dice with a given number of sides."""
    return random.randint(1, sides)

def main():
    print("\n🎲 Welcome to the Dice Roller! 🎲")
    
    while True:
        sides = int(input("Enter the number of sides on the dice (default is 6): ") or 6)
        rolls = int(input("How many dice do you want to roll? ") or 1)
        
        print("\nRolling the dice... 🎲")
        results = [roll_dice(sides) for _ in range(rolls)]
        
        print(f"Results: {', '.join(map(str, results))}")
        
        again = input("\nRoll again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! 🎲 Goodbye!")
            break

if __name__ == "__main__":
    main()
