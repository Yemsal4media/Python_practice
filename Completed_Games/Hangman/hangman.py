##
#   Hangman Game (cr8td: 280324)
#   CREATED BY YEMSAL
##

import random, string, os, time
from oxfords import oxford
from os import system

def get_word(oxford):
    word = random.choice(oxford)
    while '-' in word or ' ' in word:
        word = random.choice(oxford)
    return word.upper()

def hangman():
    word = get_word(oxford)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    print("Press ENTER to start the game")
    input("-----------------------------")

    lives = 6; score = 0; misses = 0

    while len(word_letters) > 0 and lives > 0:
        print()
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word:', ' '.join(word_list)) 
        
        user_guess = input("guess a letter: ").upper()
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
                print()
                print(f"Good Of You, '{user_guess}' is Among")
                score += 5
            else:
                lives -= 1
                score -= 2
                print(f"Letter'{user_guess}' is not in word") 

        elif user_guess in used_letters:
            print('You have already used that character, Try Agian')
        else:
            print("invalid charcter")
    if lives == 0:
        print("You died, sorry. the word is ", word)
        misses += 1
        time.sleep(2)
    else:
        print(f"You guessed the word {word} correctly!! ")
        time.sleep(2)
    print(f'Your score is {score}')
hangman()

while True:
    print()
    print()
    play_again = input("Do you want play again? [Y]es or [No] ").upper()
    play_options = ['Y', 'N', 'YES', 'NO']    
    if play_again not in play_options:
        print("You have to pick one")
        continue
    elif play_again == 'YES' or play_again == 'Y':
        hangman()
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
