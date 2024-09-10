##
#   Hangman Game (cr8td: 280324)
#   CREATED BY YEMSAL
##

import random, string, os, time
from words_list import scrable, simple_words, oxford
# from oxfords import oxford
from os import system


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
print("Press ENTER to start the game")
input("-----------------------------")
os.system('cls')

def appraise():
    appraise = ["SWEET", "EXCELLENT", "VERY GOOD", "YOU ARE A GENIOUS", "AMAZING", "MARVELIOUS", "FANTASTIC", "LOVELY", "GOOD GUESS", "I LOVE YOU" ]
    appraisal = random.choice(appraise)
    return appraisal

def depparise():
    deppraise = ["USE YOUR HEAD", "WRONG CHOICE", "YOU ARE SO DULL", "MTCHEEW", "INCORRECT CHOICE", "USELESS", "POOR", "WRONG GUESS", "DUMB HEAD", "WILL YOU WAKE UP", "YOU CAN DO BETTER THAN THAT" ]
    abuse = random.choice(deppraise)
    return abuse


def get_word(oxford): 
    easy_words = []; normal_words = []; hard_words = []
    idx = 0
    for words in oxford:
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
    return word.upper()

def hangman():
    word = get_word(oxford)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    score = 0; word_miss = 0; correct_word = 0
    live = ["H ", "A ", "N ", "G "]
    extra_lives = ["H ", "A ", "N ", "G ", "M ", "A ", "N "]
    

    while len(word_letters) > 0 and len(live) > 0:
        cut_live = len(live) - 1
        appraisal = appraise()
        abuse = depparise()
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('GUESS THE WORD:', ' '.join(word_list)) 
        print()
        print()
        print('                                                           ', ''.join(live), "Lives Left")
        print('Used letters: [', ' '.join(sorted(used_letters)), f' ]')
        print(f'                                                               {score} points')
        print()
        user_guess = input("guess a letter: ").upper()
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
                print()
                print(f"{appraisal}!, {user_guess} is Corerct")
                if len(live) != len(extra_lives):
                    live.append(extra_lives[cut_live+1])
                score += 5
            else:
                live.pop(cut_live)
                score -= 2
                print(f"{abuse}!, {user_guess} is not in word") 
        
        elif user_guess in used_letters:
            print('You have already used that character, Try Agian')
        else:
            print("invalid character")
    os.system('cls')
    if len(live) == 0:
        print()
        print("YOU DIED, Sorry the word is ", word)
        word_miss += 1
        time.sleep(4)
    else:
        print()
        print(f"You guessed the word '{word}' correctly!! ")
        correct_word += 1
        time.sleep(4)
    if len(live) >= 4:
        print(f'{2*len(live)} points for Live Well Managed')
        score += 2*len(live)
    if len(used_letters) <= len(word) and len(live) != 0:
        print('BINGO!, score + 50points ')
        score += 50
        time.sleep(4)
    return score, word_miss, correct_word

def end():
    while True:
        print()
        print()
        play_again = input("Do you want play again? [Y]es or [No] ").upper()
        play_options = ['Y', 'N', 'YES', 'NO']    
        if play_again not in play_options:
            print("You have to pick one")
            continue
        elif play_again == 'YES' or play_again == 'Y':
            the_game()
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


def the_game():
    total_game = len(oxford); scores = 0; words_miss = 0; milestone = 0

    for i in range (total_game):
        print() 
        number = (i + 1)
        print(f'WORD {number}:')
        print(f'                                                 {scores} Overall Points ')
        print(f'                                                 {3 - words_miss} RESURRECTIONS left' )
        score, word_miss, correct_word = hangman()
        words_miss = word_miss + words_miss
        scores = score + scores
        miles = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80', '85', '90',  '95', '100']
        if str(correct_word) in (miles):
            print('You reach milestone, you have been awarded ', (correct_word*2), ' points')
            scores += (number*2)
            time.sleep(3)
        if  words_miss > 3:
            print(f"YOU ARE OUT. Your Overall score is {scores}.")
            print("You can no longer be resurrected")
            break
        else:
            print(f'Your present Score is {score}')
            print(f"Your Overall score is {scores}")
            continue
the_game()

end()
