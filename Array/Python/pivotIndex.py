def pivot_index(arr):
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return left, pivot, right

arr = [4,8,2,1,5,7,6,3]
left, pivot, right = pivot_index(arr)
print("Left array: ",left)
print("Pivot element: ",pivot)
print("Right array: ",right)
