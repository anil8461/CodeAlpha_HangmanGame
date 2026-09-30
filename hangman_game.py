import random

# List of 5 words
words = ["python", "computer", "coding", "program", "developer"]

# Select a random word
word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("================================")
print("        HANGMAN GAME")
print("================================")
print("Guess the hidden word!")
print("You have 6 wrong guesses.\n")

# Main game loop
while wrong_guesses < max_guesses:

    # Display the word
    hidden_word = ""

    for letter in word:
        if letter in guessed_letters:
            hidden_word += letter
        else:
            hidden_word += "_"

    print("Word:", " ".join(hidden_word))
    print("Wrong guesses:", wrong_guesses, "/", max_guesses)

    # Check win
    if "_" not in hidden_word:
        print("\nCongratulations! You WIN!")
        print("The word was:", word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("You already guessed this letter.\n")
        continue

    # Save guessed letter
    guessed_letters.append(guess)

    # Correct or wrong
    if guess in word:
        print("Correct guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!\n")

# Lose condition
if wrong_guesses == max_guesses:
    print("GAME OVER!")
    print("The correct word was:", word)

print("\nThanks for playing!")