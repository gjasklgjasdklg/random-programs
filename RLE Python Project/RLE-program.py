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
    kjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd
    for i in range(amountOfLines)kjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd:
        enteredRLE = input("Enterkjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd line " + str(i + 1) + " > ")
        enteredRLEList.append(entkjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgderedRLE)
    print("Here is your ASCII Artkjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd:\n")
    convertToASCII()kjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd
    menu()kjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd
kjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd
kjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd
def convertToASCII():kjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd
    for i in range(len(enteredRLEkjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgdList)):
        while enteredRLEList[i][0kjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd].isdigit() == True:
            line = ""kjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd
            frequency = enteredRLkjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgdEList[i][0] + enteredRLEList[i][1]
            character = enteredRLkjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgdEList[i][2]
            rle_set = character *kjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd int(frequency)
            line = line + rle_setkjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd
            for _ in range(3):kjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd
                 enteredRLEList[ikjlfdsajlasdhgaklsdjfhalksjdfhakbfaskfasdjkfhasdfjkshadfjkhasgasigeruhgadgbajkghjjhhjgfhjgaieougthvnihwievhfjaksdvtnaiegadfjgfadkjfhwaekthaejdsgd] = enteredRLEList[i][1 : : ]
        print(line)

menu()

