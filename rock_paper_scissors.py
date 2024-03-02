# This is a game that is played against computer cr8td: 290224
import random; import time


user_win = 0
com_win = 0

options = ["rock", "paper", "scissors"]
while True:
    print("Choose Rock/Paper/scissors? "); time.sleep(1.5)
    user_choice =input("Or 'q' to quit ").lower(); time.sleep(1.5)
    if user_choice == 'q':
        break
    
    if user_choice not in options:
        print("You must choose one")
        continue
    random_num = random.randint(0, 2)
    com_choice = options[random_num]
    print ("I picked ", com_choice + ".")

    if user_choice == "rock" and com_choice == "scissors":
        print ("you won!")
        user_win += 1
    elif user_choice == "paper" and com_choice == "rock":
        print ("you won!")
        user_win += 1
    if user_choice == "scissors" and com_choice == "paper":
        print ("you won!")
        user_win += 1
    else:
        print("You lost")
        com_win += 1
if user_win == 0 and com_win == 0:
    print("I see you are scared to play with me?")
    quit()
else:
    if user_win > com_win:
        print("You are The Champoin!.")
        print("You won", user_win, "times, and I won", com_win, "times.")
        print("Nice Play, Good Day")
        quit()
    elif com_win > user_win:
        print("I am The Champoin!.")
        print("I won", com_win, "times, and you won", user_win, "times.")
        print("Nice Play, Good Day")
        quit()