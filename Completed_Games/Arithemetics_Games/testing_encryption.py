from cryptography.fernet import Fernet
from datetime import datetime

current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
current_datetime = str(current_datetime)
theDateTime = str(current_datetime)


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

Name = "Qusim"; dificulty = 'Hard'; question = 10; final_score = 2500; total_time = 200 

def create_score():
    with open("archiverer.bi", "ab") as f:
        f.write(bytes("\n"+ Name + "  " + dificulty + "  " + str(question) + "  " + str(final_score) + "  " + str(total_time) + "  " + current_datetime, 'utf-8'))
create_score()

# opening the original file to encrypt
with open('archiverer.bi', 'rb') as f:
    original = f.read()

encrypted = fer.encrypt(original)
# opening the file in write mode and 
# writing the encrypted data
with open('archiverer.bi', 'ab') as encrypted_file:
    encrypted_file.write(encrypted)

input("Press Enter to view score_ ")
# opening the encrypted file
with open('archiverer.bi', 'rb') as enc_file:
    encrypted = enc_file.readlines()
 
# decrypting the file
decrypted = fer.decrypt(encrypted)
 
# opening the file in write mode and
# writing the decrypted data
#with open('nba.csv', 'wb') as dec_file:
#    dec_file.write(decrypted)
print(decrypted)