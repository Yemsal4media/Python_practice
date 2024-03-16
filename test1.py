print ("welcome to my quiz")
while True:
    name = input("what is you name ").uppper()
    if name.isalpha():
        break
    else:
        print("that is not a name.")

while True:
    playing = input("Do you want to play? ").lower()
    if playing == "no":
        quit()
    elif playing == "yes":
        break
    else:
        print("what are you saying?")

print("Thanks for playing my dear", name)
print("okay, thats all good :)")

