'''
This game is an adventure game of many series that a player wins only with luck created 060324
'''
import random, time, os

usr_name = input("What is your name? ").upper()
print("Hello", str(usr_name), "Welcome to Lucky Adventure")
time.sleep(2)
print("----------------")
print(" NOTICE OF RISK ")
print("----------------")
print("This journey can at times involve substantial risk of injury, property damage, or death")
print("The developer shall not be responsible for any harm in the course of your journey")
time.sleep(2)
while True:
    wish = input("Do you wish to proceed? [Y]es or [N]o ").upper()
    if wish == 'YES' or wish == 'Y':
        pass
    elif wish == 'NO' or wish == 'N':
        quit()
    else:
        print("You have to pick Yes or No")
        continue
    break
time.sleep(2)
invent = ["Touch", "Cutlass", "Phone", "Cash"]
invent[3] = '$500'
print("-----------")
print(" INVENTORY ")
print("-----------")
for i in invent:
    print(i, " | ", end="  ")