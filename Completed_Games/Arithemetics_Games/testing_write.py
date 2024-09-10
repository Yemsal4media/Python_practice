from cryptography.fernet import Fernet
from datetime import datetime

current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
current_datetime = str(current_datetime)
theDateTime = str(current_datetime)

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


Name = 'qusim'; dificulty = 'hard'; question = 115; score=2550; total_time=221; 




print("Your score is ", score)
def create_score():
    with open("archiver.bin", "a") as f:
        f.write( Name + " | " + dificulty + " | " + fer.encrypt(str(question).encode()).decode() + " | " + fer.encrypt(str(score).encode()).decode() + " | " + fer.encrypt(str(total_time).encode()).decode() + " | " + current_datetime +"\n")
create_score()

print()
print("-------------")
print(" SCORE BOARD")
print("-------------")

def view_score():
    with open("archiver.bin", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            Name, dificulty, question, final_score, total_time, theDateTime = data.split("|")
            new_score = print(Name + "   " + dificulty + "   " +  fer.decrypt(str(question).encode()).decode() +" questions", "   " + fer.decrypt(str(final_score).encode()).decode() +" Points", "   " +  fer.decrypt(str(total_time).encode()).decode() +"sec", theDateTime)
            
view_score()

print()
with open('archiver.bin', 'r') as read:
    word = input('Enter the word ')
    text = read.readlines()
    new_list = []
    idx = 0
    for line in text:
        if word in line:
            new_list.insert(idx, line)
            view_score()