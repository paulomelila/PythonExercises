# A program where the computer tries to guess a number that the user has in mind between 1 and 100.
# The computer will make random guesses until it finds the correct number, and it will keep track of how many tries it took.

import random # Import the random module for generating random numbers

user_number = int(input("Enter a number between 1 and 100 for the computer to guess: ")) # Get user input

while user_number < 1 or user_number > 100: # Validate input
    user_number = int(input("Invalid input. Please enter a number between 1 and 100: "))

guess_list = [] # Initialize an empty list to store unique guesses

# Generate a list of unique random guesses between 1 and 100
while len(guess_list) < 100: # Continue until we have 100 unique guesses
    guess = random.randint(1, 100) # Generate a random guess
    if guess not in guess_list: # Check if the guess is unique
        guess_list.append(guess) # Add the unique guess to the list
    else:
        pass # If the guess is not unique, do nothing and continue

tries = 1 # Initialize tries counter to 1 (we start counting from the first guess)
for i in guess_list: # Iterate through the list of unique guesses
    if user_number == i: # Check if the guess matches the user's number
        print(f"It took {tries} tries for the computer to guess your number '{user_number}'.") # Print the number of tries
        break # Exit the loop if we found the number
    else:
        tries += 1 # Increment the tries counter if the guess was incorrect