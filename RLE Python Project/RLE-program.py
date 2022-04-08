enteredRLEList = []

def menu():
    print("""
    1: Enter RLE
    2: Display ASCII art
    3: Convert to ASCII art
    4: Convert to RLE
    5: QUIT""")

    choice = input("Enter a number > ")
    if choice == "1":
        enterRLE()
    elif choice == "2":
        pass
    elif choice == "3":
        convertToASCII()
    elif choice == "4":
        pass
    elif choice == "5":
        quit()
    else:
        print("Unrecognized input")
        menu()

def enterRLE():

    amountOfLines = int(input("How many lines of RLE do you want to input? "))
    while amountOfLines < 2:
        print("Please enter a number of lines greater than or equal to 2.")
        amountOfLines = int(input("How many lines of RLE do you want to input? "))
    
    for i in range(amountOfLines):
        enteredRLE = input("Enter line " + str(i + 1) + " > ")
        enteredRLEList.append(enteredRLE)
    print("Here is your ASCII Art:\n")
    convertToASCII()
    menu()


def convertToASCII():
    for i in range(len(enteredRLEList)):
        if len(enteredRLEList[i]) > 3:
            
        line = ""
        frequency = enteredRLEList[i][0] + enteredRLEList[i][1]
        character = enteredRLEList[i][2]
        rle_set = character * int(frequency)
        line = line + rle_set
        print(line)

menu()

