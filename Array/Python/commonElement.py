def commonElement(arr1, arr2) :
    for el in arr1:
        for me in arr2:
            if el == me:
                return True
    else:
        return False

list = [1, 2, 3, 4, 5]
list2 = [8, 7, 5, 6]

print(commonElement(list, list2))