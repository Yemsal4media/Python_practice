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



file_name = input("Enter file name: ")

try:
    with open(file_name, 'r') as file_read:
        word = input("Enter The Key word to find ").upper()
        lines = file_read.readlines()
        data = lines.rstrip()
        Name, dificulty, question, final_score, total_time, theDateTime = data.split("|")
        
        new_list = []
        idx = 0
        for line in data.split("|"):
            if word in line:
                new_list.insert(idx, Name + "   " + dificulty + "   " +  fer.decrypt(str(question).encode()).decode() +" questions", "   " + fer.decrypt(str(final_score).encode()).decode() +" Points", "   " +  fer.decrypt(str(total_time).encode()).decode() +"sec", theDateTime)
                idx += 1
    if len(new_list) == 0:
        print("\n" + word + " is not found in " + file_name + "!")
    else:
        lineLen = len(new_list)
        print("\n**** Lines containing " + word + "\n")
        for i in range(lineLen):
            print(end=new_list[i])
        print()

except:
    print("The file does not exist!")