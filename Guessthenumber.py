import random
import os

# Function to clear the screen based on the operating system
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to run the guessing game
def Guessgame():
    # Set a random number between 1 and 1000
    correct_number = random.randint(1, 1000)

    # Set guess counter to 0
    guess_counter = 0 

    # Loop until the user guesses the correct number  
    while True:
        # Get user guess
        number_guess = input("Guess the number (between 1 and 1000): ")

        # Check if the input is actually a number
        if not number_guess.isdigit():
            print("Please enter a number.")
            continue

        # Convert the input to an integer
        number_guess = int(number_guess)

        # Check if the input number is between 0 and 1000.
        if number_guess < 1 or number_guess > 1000:
            print("Please play again and only choose numbers between 1 and 1000.")
            continue

        # Increment the guess counter
        guess_counter += 1

        # Let user know if their guess was too low, too high or the right number
        if number_guess < correct_number:
            print("Too low, try again")
        elif number_guess > correct_number:
            print("Too high, try again")
        else:
            print("Whoo! That's the right number, well done!")
            print(f"It took you {guess_counter} tries to guess it!")

            # Ask if the user wants to play again
            play_again = input("Do you want to play again? (y/n): ").lower()

            # If the user does not want to play again, exit the loop
            if play_again != 'y':
                print("Goodbye!")
                break
            else:
                # If playing again, generate a new random number and reset the guess counter
                correct_number = random.randint(1, 1000)
                guess_counter = 0
                # Clear the screen for a fresh start
                clear_screen()

# Run the game
Guessgame()
