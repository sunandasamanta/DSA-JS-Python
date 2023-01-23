listOfNums = [1, 2, 3, 4, 54, 64, 76, 35, 25, 22, 98]
listOfNums.sort()

def binary_search(list, key):
    start = 0
    end = len(list)
    while start <= end:
        mid = (start + end)//2
        if list[mid] == key:
                return f'{key} found at index {mid}'
        elif list[mid] > key:
            end = mid - 1
        else:
            start = mid + 1

    return f'{key} not found'

print(binary_search(listOfNums, 35))



# ChatGPT answer

# listOfNums = [1, 2, 3, 4, 54, 64, 76, 35, 25, 22, 98]
# listOfNums.sort()
# 
# def binary_search(list, key):
#     start = 0
#     end = len(list) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if list[mid] == key:
#             return mid
#         elif list[mid] > key:
#             end = mid - 1
#         else:
#             start = mid + 1

#     return -1

# print(binary_search(listOfNums, 35))