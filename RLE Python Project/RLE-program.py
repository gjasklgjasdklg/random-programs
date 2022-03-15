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
        pass
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
    
    for i in range(1, (amountOfLines + 2)):
        enteredRLE = input("Enter line {} > ").format(i)
        enteredRLEArray = enteredRLE.split("")


menu()