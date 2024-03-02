import random
while True:
    print("welcome to Guess the number game!")
    maxn = input("Enter maximum number of guess greater than 0 or 'q' to QUIT ")
#checking if user input is digit number
    if maxn == 'q':
        quit()
    if maxn.isdigit():
        maxn = int(maxn)
    if maxn <= 0:
        print('Enter real number Greater than 0')
        continue
    elif print('enter a real number not Alphabet'):
        continue
    else:
        break
# Computer choose a hidden random number that they will guess 
print("You will now guess a number between 0 and ", maxn)
hidden_num = random.randint(0, maxn)
user_win = 0
com_win = 0

# Taking user Guess and checking if its digit

while True:
    user_guess = input('Now Guess a number! ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('enter a real number next time')
        continue
# Tracking user guess position
    if user_guess == number:
        print('You are Dawn Correct')
        break
    elif user_guess > number:
        print('you are above the number')
    else:
        print('you are Below the number')

if chances == 1:
    print("BULLS EYE")
else:
    print("you got the number in ", chances ,"Guesses")
