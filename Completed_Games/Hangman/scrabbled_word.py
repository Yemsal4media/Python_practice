import random

# List of words to choose from
word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'ban', 'ate', 'app', 'pale', 'lap', 'berry', 'elder']

# Choose a random word from the list
chosen_word = random.choice(word_list)

# Scramble the chosen word
scrambled_word = ' '.join(random.sample(chosen_word, len(chosen_word)))

# Display the scrambled word
print(f"Scrambled word: {scrambled_word}")

# Load a list of valid words (for simplicity, using the word_list)
valid_words = set(word_list)

# Initialize a set to store user's correct guesses
correct_guesses = set()

# Game loop
while True:
    user_guess = input("Guess a word from the scrambled letters (or type 'exit' to quit): ").lower()
    if user_guess == 'exit':
        break
    if user_guess in valid_words and set(user_guess).issubset(set(chosen_word)):
        if user_guess in correct_guesses:
            print("You've already guessed that word!")
        else:
            print("Correct!")
            correct_guesses.add(user_guess)
    else:
        print("That's not a valid word from the scrambled letters.")

# End of game summary
print(f"\nThank you for playing! You guessed {len(correct_guesses)} words correctly.")
for word in correct_guesses:
    print(word)
