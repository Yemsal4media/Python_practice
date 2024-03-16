import random, time, os
from cryptography.fernet import Fernet
from datetime import datetime

current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
current_datetime = str(current_datetime)
'''
key = Fernet.generate_key()
fer = Fernet(key)
'''
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
b'S1mSM10A1E40PbTtPLHg2EhkGOiXXGBCMFNMB6sERkY='
'''
### i already generate a key i want to be using
def write_key():
    key = b'S1mSM10A1E40PbTtPLHg2EhkGOiXXGBCMFNMB6sERkY='
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



min_guess = 2; 
max_guess = 0; 
Total_prob= 1000000; score = 0
misses = 0
chance_left = 5

while True:
    Name = input("What is your name? ").upper()
    if Name.isalpha():
        Name = str(Name)
        break
    else:
        print("That can't be your real name")
        print("Your name can not contain Space or any other character")
        continue
print()
print("Welcome to ARITHEMTIC SPEED GAME, " + Name)
print()
print("----------------")
print("RULES ARE SIMPLE")
print("----------------")
print("1) There are unlimited random questions")
print("2) You score 5point for each correct answer and lose 2 point for each wrong answer")
print("3) Once you miss 5 questions you are out")
print("4) You earn 10 points as you reach Milestones")
print("4) I will advice you to be fast, becuase you will be awarded 50 points for Speed")
print("6) You are expected to use not more than 3 seconds per question to win SPEED BONUS")
print("5) GOOD LUCK")
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

bin_oprtn = ["-", "+", "*"]

def Binary_operation():
    LHS= random.randint(min_guess, max_guess)
    RHS= random.randint(min_guess, max_guess)
    bin_oprtns = random.choice(bin_oprtn)

    expr = str(LHS) + " " + bin_oprtns + " " + str(RHS)
    answer = eval(expr)
    return expr, answer

print("Press ENTER to start the game")
input("-----------------------------")
start_time = time.time()
for i in range(Total_prob):
    os.system('cls')
    expr, answer = Binary_operation()
    if misses == 5:
        print("You have missed 5, YOU ARE OUT OF THE GAME")
        break
    else:
        while True:
            print()
            print("Your present Score is ", score )
            print(f"You have missed {misses} questions")
            question = str(i + 1)
            print()
            print()
            guess = input("QUESTION " + question + ": " + expr + " = ")
            if question == str(10) or question == str(30):
                print("MILESTONE REACHED! 20points Gained")
                score += 20
            elif question == str(50) or question == str(100):
                print("MILESTONE REACHED! 20points Gained")
                score += 20
            elif question == str(200) or question == str(500):
                print("MILESTONE REACHED! 20points Gained")
                score += 20
                continue
            if guess == str(answer):
                score += 5
                break
            else:
                if misses == 5 or chance_left == 0:
                    break
                else:
                    print("Wrong, Try again")
                    score -= 2 
                    misses += 1
                    chance_left = 5 - misses
                    print("You have ", chance_left, " chances Left")
                    continue                    
end_time = time.time()
total_time = round((end_time - (start_time + 5)), 1)
if dificulty == 'E' or dificulty == 'EASY':
    Speed_time = (3 * int(question))
elif dificulty == 'N' or dificulty == 'NORMAL':
    Speed_time = (4 * int(question))
elif dificulty == 'H' or dificulty == 'HARD':
    Speed_time = (7 * int(question))

if total_time <= Speed_time and int(question) > 10:
    diff = Speed_time - total_time 
    diff_final = round((diff * int(question)) + 50)
    score = score + diff_final
    print("You have been Awarded SPEED BONUS of ", diff_final, "points.")
else:
    pass
print("Congratulation", Name)
print("You attempted ", question, "questions")
print("Your score is ", score , "On a difficulty level ", dificulty)
print("You are supposed to finish in ", Speed_time, "seconds, But You finished in ", total_time, "seconds")

def create_score():
    with open("score_board.txt", "a") as f:
        f.write( Name + " | " + dificulty + " | " + fer.encrypt(str(question).encode()).decode() + " | " + fer.encrypt(str(score).encode()).decode() + " | " + fer.encrypt(str(total_time).encode()).decode() + " | " + current_datetime+"\n")

create_score()

print()
print("-------------")
print(" SCORE BOARD")
print("-------------")

def view_score():
    with open('score_board.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            Name, dificulty, question, score, total_time, theTime = data.split("|")
            print(Name + dificulty + "   " +  fer.decrypt(str(question).encode()).decode() +" questions" + "   " + fer.decrypt(str(score).encode()).decode() +" Points" + "   " +  fer.decrypt(str(total_time).encode()).decode() +"sec" + "   " + theTime)
view_score()
print()
print()
print()
print()
print()
print("Thank you for playing, I am Yemsal")
input("Press Enter to quit______ ")
quit
