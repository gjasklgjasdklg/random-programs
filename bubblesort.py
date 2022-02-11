def bubbleSort(array):
    swap = True
    end = len(array)
    while swap == True:
        swap = False
        for i in range(1, end):
            if array[i-1] > array[i]:
                temp = array[i]
                array[i] = array[i-1]
                array[i-1] = temp
                swap = True
        end -= 1
examScores = [92,55,84,48,72,90,87,54,67,75]
print(examScores)
bubbleSort(examScores)
print(examScores)