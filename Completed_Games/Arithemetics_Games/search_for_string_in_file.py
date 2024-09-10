file_name = input("Enter file name: ")

try:
    file_read = open(file_name, 'r')
    text = input("Enter The Key word to find ").upper()
    lines = file_read.readlines()

    new_list = []
    idx = 0
    for line in lines:
        if text in line:
            new_list.insert(idx, line)
            idx += 1
    file_read.close()

    if len(new_list) == 0:
        print("\n" + text + " is not found in " + file_name + "!")
    else:
        lineLen = len(new_list)
        print("\n**** Lines containing " + text + "\n")
        for i in range(lineLen):
            print(end=new_list[i])
        print()

except:
    print("The file does not exist!")