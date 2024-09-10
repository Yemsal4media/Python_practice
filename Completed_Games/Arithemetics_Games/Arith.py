import random, time, os
from cryptography.fernet import Fernet
from datetime import datetime

current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
current_datetime = str(current_datetime)
theDateTime = str(current_datetime)
'''
key = Fernet.generate_key()
fer = Fernet(key)

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
b'S1mSM10A1E40PbTtPLHg2EhkGOiXXGBCMFNMB6sERkY='
'''
### i already generate a key i want to be using
def write_key():
    key = b'S0PbTtP(YemsalDesignedTheGame)LHGCMFNMB6sERkY='
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
load_key()

key = load_key()
fer = Fernet(key)


min_guess = 2 
max_guess = 0

# Username collection
while True:
    Name = input("What is your name? ").upper()
    if Name.isalpha():
        Name = str(Name)
        break
    else:
        print("That can't be your real name")
        print("Your name can not contain Space or any other character")
        continue

#Game Rules
print()
print("Welcome to ARITHEMTIC SPEED GAME, " + Name)
print()
print("----------------")
print("RULES ARE SIMPLE")
print("----------------")
print("1) There are unlimited random questions")
print("2) You score 5point for each correct answer and lose 2 point for each wrong answer")
print("3) Once you miss 5 questions, IT'S GAME OVER")
print("4) You also earn additional points as you reach Milestones")
print("5) I will advice you to be fast, because you will be awarded HUGE points for Speed")
print("GOOD LUCK!")

#Difficulty Levels
print()
while True:
    print("Enter levels of Difficulty")
    dificulty = input("[E]asy, [N]ormal, [H]ard ").upper()
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

if dificulty == 'E' or dificulty == 'EASY':
    max_guess = 7
elif dificulty == 'N' or dificulty == 'NORMAL':
    max_guess = 15
else:
    min_guess = 5
    max_guess = 20

#The Game
bin_oprtn = ["-", "+", "*"]

def Binary_operation():
    LHS= random.randint(min_guess, max_guess)
    RHS= random.randint(min_guess, max_guess)
    bin_oprtns = random.choice(bin_oprtn)

    expr = str(LHS) + " " + bin_oprtns + " " + str(RHS)
    answer = eval(expr)
    return expr, answer

def The_game():
#Main Game
    misses = 0
    Total_prob = 1000000; score = 0; final_score = 0
    misses = 0; milestone = 0
    chance_left = 5
    print("Press ENTER to start the game")
    input("-----------------------------")
    start_time = time.time()
    for i in range(Total_prob):
        os.system('cls')
        expr, answer = Binary_operation()
        if misses > 4:
            print("You have missed 5, YOU ARE OUT OF THE GAME")
            break
        else:
            while True:
                print()
                print(f"You have missed {misses} questions, {chance_left} chances left")
                print(f"Your present Score is {score}, Milestone score is {milestone}")
                question = str(i + 1)
                print()
                print()          
                guess = input("QUESTION " + question + ": " + expr + " = ")
                if question == str(10) or question == str(30):
                    print("MILESTONE REACHED! 20points Gained")
                    score += 100; milestone += 100
                elif question == str(50) or question == str(100):
                    print("MILESTONE REACHED! 40points Gained")
                    score += 400; milestone += 400
                elif question == str(200) or question == str(500):
                    print("MILESTONE REACHED! 80points Gained")
                    score += 800; milestone += 800
                    continue
                if guess == str(answer):
                    score += 5
                    break
                else:
                    if misses > 4 or chance_left < 1:
                        break
                    else:
                        print("Wrong, Try again")
                        score -= 2 
                        misses += 1
                        chance_left -= 1
                        print("You have ", chance_left, " chances Left")
                        continue                    
    end_time = time.time()
    total_time = round((end_time - (start_time + 5)), 1)
    if dificulty == 'E' or dificulty == 'EASY':
        Speed_time = (3 * int(question))
    elif dificulty == 'N' or dificulty == 'NORMAL':
        Speed_time = (4 * int(question))
    elif dificulty == 'H' or dificulty == 'HARD':
        Speed_time = (5 * int(question))

    if total_time <= Speed_time and int(question) > 10:
        diff = Speed_time - total_time 
        diff_final = round(diff * int(question))
        final_score = score + diff_final
        print("You have been Awarded SPEED BONUS of ", diff_final, "points.")
    else:
        pass
    print()
    print("Nice Play", Name)
    print("You attempted ", question, "questions, On a difficulty level", dificulty)
    print("You are supposed to finish in ", Speed_time, "seconds, But You finished in ", total_time, "seconds")
    if total_time <= Speed_time and int(question) > 10:
        print("Your score is ", score , "plus your speed Bonus", diff_final , "= ", final_score)
        def create_score():
            with open("archive.bi", "a") as f:
                f.write( Name + " | " + dificulty + " | " + fer.encrypt(str(question).encode()).decode() + " | " + fer.encrypt(str(final_score).encode()).decode() + " | " + fer.encrypt(str(total_time).encode()).decode() + " | " + current_datetime +"\n")
        create_score()
    else:
        print("Your score is ", score)
        def create_score():
            with open("archive.bi", "a") as f:
                f.write( Name + " | " + dificulty + " | " + fer.encrypt(str(question).encode()).decode() + " | " + fer.encrypt(str(score).encode()).decode() + " | " + fer.encrypt(str(total_time).encode()).decode() + " | " + current_datetime +"\n")
        create_score()

    print()
    print("-------------")
    print(" SCORE BOARD")
    print("-------------")

    def view_score():
        with open("archive.bi", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                Name, dificulty, question, final_score, total_time, theDateTime = data.split("|")
                print(Name + "   " + dificulty + "   " +  fer.decrypt(str(question).encode()).decode() +" questions", "   " + fer.decrypt(str(final_score).encode()).decode() +" Points", "   " +  fer.decrypt(str(total_time).encode()).decode() +"sec", theDateTime)
    view_score()
    print()
The_game()

while True:
    print()
    print()
    play_again = input("Do you want play again? [Y]es or [No] ").upper()
    play_options = ['Y', 'N', 'YES', 'NO']    
    if play_again not in play_options:
        print("You have to pick one")
        continue
    elif play_again == 'YES' or play_again == 'Y':
        The_game()
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
