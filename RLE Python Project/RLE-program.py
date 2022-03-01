quit_program = False

def menu():

    print("""
    1: Enter RLE
    2: Display ASCII art
    3: Convert to ASCII art
    4: Convert to RLE
    5: QUIT""")

    choice = input("Enter a number > ")
    if choice == "1":
        pass
    if choice == "2":
        pass
    if choice == "3":
        pass
    if choice == "4":
        pass
    if choice == "5":
        print("You will regret that decision...") 
        quit_program == True

while quit_program == False:
    menu()