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
        displayASCII()
    elif choice == "3":
        RLE_fileToASCII()
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
    ASCII_output = []
    for i in range(len(enteredRLEList)):
        line = enteredRLEList[i]
        new_line = ''
        i = 0
        while i <= len(line) - 3:
            frequency = line[i] + line[i + 1]
            character = line[i + 2]
            rle_set = str(character) * int(frequency)
            new_line = new_line + rle_set
            i = i + 3
        ASCII_output.append(new_line)
    for i in range(len(ASCII_output)):
        print(ASCII_output[i])

def displayASCII():
    file_name = input("Enter the filename that you would like to open (include extension). If the file is not in the same directory as this file, please provide the full path: ")
    with open(file_name, "r") as ASCII_art:
        art = ASCII_art.read()
    print(art)
    menu()

def RLE_fileToASCII():
    RLE_file = input("Enter the filename that you would like to open (include extension). If the file is not in the same directory as this file, please provide the full path: ")
    with open(RLE_file, "r") as openedFile:
        for count, line in enumerate(openedFile):
            enteredRLE = line
            enteredRLEList.append(enteredRLE)
    convertToASCII()
    menu()

menu()