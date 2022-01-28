coding_gurus = [
    "Adam",
    "Banjo",
    "Claire",
    "Dave",
    "Edzel",
    "Frank",
    "Graham",
    "Harry",
    "Imogen",
    "James"
]

chosen_guru = input("Enter a username: ")

if chosen_guru in coding_gurus:
    print("The guru " + chosen_guru + " will be in contact shortly.")
else:
    print("That username does not belong to a coding guru.")

