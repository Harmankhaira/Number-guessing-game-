import random

def guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("🎮 Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1
            
            if guess < number:
                print("📈 Too low! Try a higher number.")
            elif guess > number:
                print("📉 Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {number}")
                return
                
        except ValueError:
            print("❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid input
    
    print(f"\n💥 Game Over! The number was {number}")
    print("Better luck next time!")

if __name__ == "__main__":
    guessing_game()
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == 'y':
        guessing_game()
