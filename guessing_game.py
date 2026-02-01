"""
Number Guessing Game
A fun interactive game to practice Python!
"""

import random

def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("=" * 40)
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print(f"\nI'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                attempts -= 1  # Don't count invalid guesses
                continue
            
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                if attempts <= 3:
                    print("Amazing! You're a mind reader! 🧠")
                elif attempts <= 5:
                    print("Great job! Well done! 👏")
                else:
                    print("Phew! That was close! 😅")
                return True
            elif guess < secret_number:
                print(f"📈 Too low! Attempts remaining: {max_attempts - attempts}")
            else:
                print(f"📉 Too high! Attempts remaining: {max_attempts - attempts}")
                
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"\n😢 Game Over! The number was {secret_number}")
    return False

def main():
    print("\n" + "=" * 40)
    print("   PYTHON NUMBER GUESSING GAME")
    print("=" * 40)
    
    play_again = True
    wins = 0
    games = 0
    
    while play_again:
        games += 1
        if play_game():
            wins += 1
        
        print(f"\n📊 Score: {wins}/{games} games won")
        
        response = input("\nPlay again? (yes/no): ").lower().strip()
        play_again = response in ['yes', 'y']
    
    print("\n👋 Thanks for playing! See you next time!")

if __name__ == "__main__":
    main()
