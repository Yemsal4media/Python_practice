# This is a game that generates random number cr8td: 290224
import random
print(" WELCOME TO GUESS THE NUMBER GAME")
randtop = input('Type your upperbound number ')

# checking if the number is Digit and none zero

if randtop.isdigit():
    randtop = int(randtop)

    if randtop <= 0:
        print('Enter real number next time')
        quit()
else:
    print('enter a real number')
    quit()
number = random.randrange(0, randtop)

# Taking user Guess and checking if its digit
chances = 0

while True:
    chances += 1
    user_guess = input('Guess a number! ')
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
