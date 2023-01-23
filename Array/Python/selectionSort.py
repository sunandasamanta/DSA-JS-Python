listOfNums = [5, 14, 54, 64, 76, 35, 2, 3, 1, 25, 22, 98]


def selectionSort(arr):
    sortedArray = []
    while len(arr) > 0:
        min = arr[0]
        minIndex = 0
        for i in range(1, len(arr)):
            if arr[i] < min:
                min = arr[i]
                minIndex = i
        sortedArray.append(min)
        arr.pop(minIndex)
    return sortedArray

result = selectionSort(listOfNums)
print(result)
