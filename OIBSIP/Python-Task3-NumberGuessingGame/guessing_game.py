# Number Guessing Game
import random

def play_game():
    print("--- Number Guessing Game ---")
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too Low! Try a higher number.")
        elif guess > secret_number:
            print("Too High! Try a lower number.")
        else:
            print(f"\nCongratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break
    else:
        print(f"\nGame Over! The secret number was {secret_number}.")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
