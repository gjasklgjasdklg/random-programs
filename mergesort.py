def merge_sort(array):
    print("Split", array)
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        a = 0
        b = 0
        c = 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                array[c] = left[a]
                a += 1
            else:
                array[c] = right[b]
                b += 1
            c += 1

        while a < len(left):
            array[c] = left[a]
            a += 1
            c += 1

        while b < len(right):
            array[c] = right[b]
            b += 1
            c += 1
        print("Merge", array)#

examScores = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
print(examScores)
merge_sort(examScores)
print(examScores)