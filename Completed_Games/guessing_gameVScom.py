##
#   The game where Player and Computer have to guess a number and track the one that got it first (cr8td: 020324)
#   CREATED BY YEMSAL
##
import random, time, os
while True:

    print("################# WELCOME TO GUESS THE NUMBER GAME!##############"); time.sleep(0.2)
    maxn = input("Enter maximum number of guess greater than 0 or 'q' to QUIT ")
    if maxn.lower() == 'q':
        quit()
    maxscore = input ("What is the Maximum Score to win the game? ")

    # checking if user input is digit number
    if maxscore.lower() == 'q':
        quit()
    elif maxn.isdigit() and maxscore.isdigit():
        maxn = int(maxn) 
        maxscore = int(maxscore)
    else:
        print('enter a real number not Alphabet')
        continue 
    if maxn <= 0:
        print('Enter real number Greater than 0')
        continue
    else:
        break

user_win = 0
com_win = 0
    # Taking user Guess and checking if its digit
    
while True:
    os.system('cls')
    score_board = [user_win, com_win]
    # Computer choose a hidden random number that they will guess 
    # Its inside loop so that new number will be genrated each time they play again
    time.sleep(2)
    print()
    print ("SCORE BOARD")
    print("-------------")
    print ('user vs com', score_board)
    print ()
    if maxscore <= 5:
        if user_win == 4 and com_win == 4:
            time.sleep(2)
            print("DEUCE!")
            user_win = (user_win - 1)
            com_win = (com_win - 1)
            score_board = [user_win, com_win]
            print()
            print ("SCORE BOARD")
            print("-------------")
            print ('user vs com', score_board)
            print ()
    else:
        if maxscore > 5:
            if user_win == 9 and com_win == 9:
                print("DEUCE!")
                user_win = user_win - 1
                com_win = com_win - 1
                score_board = [user_win, com_win]
                print()
                print ("SCORE BOARD")
                print("-------------")
                print ('user vs com', score_board)
                print ()

    if user_win == maxscore or com_win == maxscore:
            time.sleep(5)
            os.system('cls')
            print("#### GAME OVER ####")
            if user_win > com_win:
                print("YOU WIN!")
                print("You won with ", user_win, "vs", com_win)
            elif user_win < com_win:
                print("YOU LOOSE!")
                print("I won with ", com_win, "vs", user_win)
            elif user_win == com_win:   
                print("it's a Tie")
                print (score_board)
                print("Nice Play")
            time.sleep(3)
            for i in range(10, 0, -1):
                print(i, end=' ')
                time.sleep(1)
            quit()
    else:
        print("You will now guess a number between 0 and ", maxn)
    hidden_num = random.randint(0, maxn)
    # The Game in the loop
    while True:
        com_guess = random.randint(0, maxn)
        print()
        user_guess = input('Guess your number! '); time.sleep(0.2)
        print("My own guess is ", com_guess); time.sleep(1)
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print('enter a real number next time')
            continue
# Tracking user guess position
        
            # When Both player and computer wins
        if user_guess == hidden_num and com_guess == hidden_num:
            print("Its a tie!"); time.sleep(0.5)
            print("We are both Correct. The Hidden number is ", hidden_num); time.sleep(0.5)
            print("ONE POINT for you and I"); time.sleep(3)
            user_win += 1
            com_win += 1
            break
            
        # When only player wins
        if user_guess == hidden_num and com_guess != hidden_num:
            print('You are Correct, The hidden number is', hidden_num); time.sleep(0.5)
            print("ONE POINT for you"); time.sleep(3)
            user_win += 1
            break
            
        # When only computer wins
        if user_guess != hidden_num and com_guess == hidden_num:
            print('You are wrong, The hidden number is', hidden_num); time.sleep(0.5)
            print("ONE POINT for me ahhahhahh!"); time.sleep(3)
            com_win += 1
            break
            
        # When none of the player wins, so they try again giving player more adavatage over computer because of clues added
        if user_guess != hidden_num and com_guess != hidden_num:
            print('We are both wrong, Lets guess again'); time.sleep(3)
        if user_guess > hidden_num:
            print('The number is SMALLER than your guess')
        else:
            print('The number is LARGER than your guess')
        time.sleep(3)  
        continue
    