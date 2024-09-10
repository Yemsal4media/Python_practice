import random

def choose_word():
    word_list = ['python', 'hangman', 'programming', 'development', 'challenge']
    return random.choice(word_list)

def display_board(hidden_word, attempts):
    print("Word to guess: " + ' '.join(hidden_word))
    print("\nAttempts remaining: " + str(attempts))

def get_guess():
    return input("Enter a letter: ").lower()

def update_hidden_word(word, hidden_word, guess):
    return [guess if word[i] == guess else hidden_word[i] for i in range(len(word))]

def play_hangman():
    word = choose_word()
    hidden_word = ['_' for _ in word]
    attempts = len(word) + 3
    guessed_letters = set()

    while attempts > 0 and '_' in hidden_word:
        display_board(hidden_word, attempts)
        guess = get_guess()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            hidden_word = update_hidden_word(word, hidden_word, guess)
            print("Good guess!")
        else:
            attempts -= 1
            print("Oops! Wrong guess.")

        if '_' not in hidden_word:
            print("Congratulations! You've guessed the word: " + word)
            break

    if '_' in hidden_word:
        print("Game over! The word was: " + word)

if __name__ == "__main__":
    play_hangman()
