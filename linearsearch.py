def linearsearch (myItem,myList):
    match = False
    position = 0
    while position < len(myList) and match == False:
        if myList [position] == myItem:
            match = True
        position = position + 1
    return match

myItem = int(input("select a number: "))
myList = [1,2,3,4,5,6,7,8,9,10]
print(linearsearch(myItem,myList))
