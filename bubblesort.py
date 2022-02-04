def bubbleSort(array):
    swap = True
    while swap == True:
        swap = False
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                temp = array[i]
                array[i] = array[i-1]
                array[i-1] = temp
                swap = True

examScores = [92,55,84,48,72,90,87,54,67,75]
print(examScores)
bubbleSort(examScores)
print(examScores)