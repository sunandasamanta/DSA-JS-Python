listOfNums = [1, 2, 3, 4, 54, 64, 76, 35, 25, 22, 98]

def linear_search (arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return f"{key} exists at index {i}."

    return f"{key} doest not exist in the list."

print(linear_search(listOfNums, 64))