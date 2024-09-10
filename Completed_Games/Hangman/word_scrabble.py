import random, string, os, time
from words_list import scrable, simple_words, oxford
# from oxfords import oxford
from os import system

# Bringing the two list to become one
word_list = []
for i in oxford:
    word_list.append(i)
for j in simple_words:
    if j not in word_list:
        word_list.append(j)
    
#Scoring System
def scrabble_score(word):
    SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}
    total = 0

    for letter in word:
        print(letter, '-', SCORES[letter])
        total += SCORES[letter]
    return total


#Difficulty level
while True:
    print("Enter levels of Difficulty")
    dificulty = input("[E]asy, [N]ormal, [H]ard___").upper()
    if dificulty == 'E':
        dificulty = "EASY"
    elif dificulty == 'N':
        dificulty = 'NORMAL'
    elif dificulty == 'H':
        dificulty = 'HARD'
    options = ['EASY', 'NORMAL', 'HARD']    
    if dificulty not in options:
        print("You have to pick one level")
        continue
    else:
        break
print()
print()


#If Your are correct, you will be Appraised
def appraise():
    appraise = ["SWEET", "EXCELLENT", "VERY GOOD", "YOU ARE A GENIOUS", "AMAZING", "MARVELIOUS", "FANTASTIC", "LOVELY", "GOOD GUESS", "I LOVE YOU" ]
    appraisal = random.choice(appraise)
    return appraisal


#If Your are wrong, you will be embarassed
def depparise():
    deppraise = ["USE YOUR HEAD", "WRONG CHOICE", "YOU ARE SO DULL", "MTCHEEW", "INCORRECT CHOICE", "USELESS", "POOR", "WRONG GUESS", "DUMB HEAD", "WILL YOU WAKE UP", "YOU CAN DO BETTER THAN THAT" ]
    abuse = random.choice(deppraise)
    return abuse


#Get words according to difficulty level
def get_word(word_list): 
    easy_words = []; normal_words = []; hard_words = []
    idx = 0
    for words in word_list:
        if len(words) <= 5 and len(words) >= 3:
            easy_words.insert(idx, words)
            idx += 1
        elif len(words) >= 3 and len(words) <= 6:
            normal_words.insert(idx, words)
            idx += 1
        elif len(words) >= 5:
            hard_words.insert(idx, words)
            idx += 1

    if dificulty == 'E' or dificulty == 'EASY':
        word = random.choice(easy_words)
        while '-' in word or ' ' in word:
            word = random.choice(easy_words)
    elif dificulty == 'N' or dificulty == 'NORMAL':
        word = random.choice(normal_words)
        while '-' in word or ' ' in word:
            word = random.choice(normal_words)
    else:
        word = random.choice(hard_words)
        while '-' in word or ' ' in word:
            word = random.choice(hard_words)
    return word.lower()


def scrablle():
    
    # Choose a random word from the list
    word = get_word(word_list)

    # Scramble the chosen word
    scrambled_word = ' '.join(random.sample(word, len(word)))

    # Initialize a set to store user's correct guesses
    correct_guesses = set()
    wrong_guess = set()
    turbo = 0;  score = 0; shuffle = 0
    # Game loop
    while turbo >= 0:
        appraisal = appraise()
        abuse = depparise()
        # Display the scrambled word
        print(f'                                                                                     score = {score}')
        print(f'                                                                                     Turbo = {turbo}')
        print(f'                                                                                     Shuffle = {shuffle}')
        print(f"Scrambled word: {scrambled_word.upper()}")
        print()
        # Displays words that have been accepted as correct
        print('Used Words :')
        for i in correct_guesses:
            print(i, end=", ")  
        print()
        print('Wrong Words :')
        for j in wrong_guess:
            print(j, end=", ")  
        print()

        user_guess = input("\nGuess a word from the scrambled letters (or type '1' to quit or '2' to Shuffle): ").lower()
        if user_guess == '1':
            break
        elif user_guess == '2':
            scrambled_word = ' '.join(random.sample(word, len(word)))
            shuffle += 1
            if shuffle == 2:
                turbo -= 1
                shuffle = 0
        else:
            if user_guess in set(scrable) and set(user_guess).issubset(set(word)):
                if user_guess in correct_guesses:
                    print("You've already guessed that word!")
                    turbo -= 1
                else:
                    if len(user_guess) == len(word):
                        print(f"{appraisal}! BINGO SHOT!")
                        total = scrabble_score(user_guess)
                        print(f'{total+50} points for Your Word "{user_guess}".')
                        correct_guesses.add(user_guess)
                        score += total+50
                        turbo += 1
                    else:
                        print(f"{appraisal}")
                        print()
                        total = scrabble_score(user_guess)
                        print(f'{total} points for Your Word "{user_guess}".')
                        correct_guesses.add(user_guess)
                        score += total
                        turbo += 1
            else:
                print(f"{abuse}! That's not a valid word from the scrambled letters.")
                wrong_guess.add(user_guess)
                turbo -= 1

    # End of game summary
    print(f"\nYou guessed {len(correct_guesses)} words correctly and your score is {score}")
    for word in correct_guesses:
        print(word, end=", ")
    while True:
        print()
        print()
        play_again = input("Do you want play again? [Y]es or [No] ").upper()
        play_options = ['Y', 'N', 'YES', 'NO']    
        if play_again not in play_options:
            print("You have to pick one")
            continue
        elif play_again == 'YES' or play_again == 'Y':
            scrablle()
        else:
            break

    print()
    print()
    print()
    print()
    print("Thank you for playing, I am Yemsal")
    print("Feel free to recommend and further Adjustments")
    input("Press Enter to quit______ ")
    quit()
scrablle()