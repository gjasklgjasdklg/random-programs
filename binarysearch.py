def binary_search(myItem, myList):
    match = False
    bottom = 0
    top = len(myList) - 1
    while bottom <= top and match == False:
        middle = (bottom + top) // 2
        if myList[middle] == myItem:
            match = True
        elif myList[middle] < myItem:
            bottom = middle + 1
        else:
            top = middle - 1
    print(match)

myItem = int(input("Please select a number: "))
myList = [1,2,3,4,5,6,7,8,9,10]
binary_search(myItem,myList)