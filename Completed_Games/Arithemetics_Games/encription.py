from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
'''

def create_score():
    with open("score_board.txt", "a") as f:
        f.write( Name + "  |  " + dificulty + "  |  " + fer.encrypt(str(question).encode()).decode() + " |  " + fer.encrypt(str(score).encode()).decode() + " |  " + fer.encrypt(str(total_time).encode()).decode() +"\n")