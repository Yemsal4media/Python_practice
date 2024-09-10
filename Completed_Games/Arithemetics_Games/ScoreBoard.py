# VIew Score Board without playing the game
import os
from cryptography.fernet import Fernet

###You cant change this key except you change the writing key in the Arith.py file. otherwise you won't be able to decrypt the scoreboard file.

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



def view_score():
    os.system('cls')
    print()
    print("-------------")
    print(" SCORE BOARD")
    print("-------------")
    with open("archive.bi", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            Name, dificulty, question, final_score, total_time, theDateTime = data.split("|")
            print(Name + "   " + dificulty + "   " +  fer.decrypt(str(question).encode()).decode() +" questions", "   " + fer.decrypt(str(final_score).encode()).decode() +" Points", "   " +  fer.decrypt(str(total_time).encode()).decode() +"sec", theDateTime)

def view_player_score():
    try:
        file = open('archive.bi', 'r')
        player = input("Enter players name or the Difficulty played ").upper()
        os.system('cls')
        lines = file.readlines()

        new_list = []
        idx = 0
        for line in lines:
            if player in line:
                data = line.rstrip()
                player, dificulty, question, final_score, total_time, theDateTime = data.split("|")
                new_lines = player + "   " + dificulty + "   " +  fer.decrypt(str(question).encode()).decode() +" questions", "   " + fer.decrypt(str(final_score).encode()).decode() +" Points", "   " +  fer.decrypt(str(total_time).encode()).decode() +"sec", theDateTime
                new_list.insert(idx, new_lines)
                idx += 1
        file.close()        
        if len(new_list) == 0:
            print("\n" + player + " is not found on the Scoreboard!")
        else:
            lineLen = len(new_list)
            print("\n****You are viewing The Scores of " + player + "\n")
            print()
            print("-------------")
            print(" SCORE BOARD")
            print("-------------")
            for i in range(lineLen):
                print(end=new_list(i))
            print()
    except:
        print("The file does not exist!")
           
def scoreboard():
    os.system('cls')
    while True:
        view_scores = input("Press 1 for 'ALL SCORES' or 2 for 'A PLAYER'S SCORE'_")
        if view_scores == '1' or view_scores == '2':
            if view_scores == '2':
                view_player_score()
                while True:
                    print()
                    search_again = input("Do you want search again? [Y]es or [No] ").upper()
                    options = ['Y', 'N', 'YES', 'NO']    
                    if search_again not in options:
                        print("You have to pick one")
                        continue
                    elif search_again == 'YES' or search_again == 'Y':
                        scoreboard()
                    else:
                        break    
                break
            else:
                view_scores == '1'
                view_score()
                print()
                break
        else:
            print("Wrong Choice!")
            continue
        
scoreboard()
print()
print()
print()
print()
print()
print("Thank you for playing, I am Yemsal")
print("Feel free to recommend and further Adjustments")
input("Press Enter to quit______ ")
quit()
