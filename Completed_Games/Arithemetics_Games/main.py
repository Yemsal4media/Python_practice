# main Control

while True:
    Name = input("What is your name? ")
    if Name.isalpha():
        break
    else:
        print("That can't be your real name")
        continue
print()
print("Welcome to Arithmetic Skill Game, " + Name)
print()