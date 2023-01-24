"""Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list as the sort progresses."""

"""Here is an example of bubble sort in Python:"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))
# In this example, the function bubble_sort takes an input array and sorts it in ascending order using the bubble sort algorithm. The outer loop iterates through the array, and the inner loop compares adjacent elements and swaps them if they are in the wrong order. This process is repeated until the array is sorted.
