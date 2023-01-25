
# Introduction to Asymptotic Notation

## Topics

1. Time complexity of common algorithms (e.g. bubble sort, insertion sort, quicksort, etc.)
1. Big O notation (e.g. O(1), O(n), O(n^2), O(log n), etc.)
1. Big Omega notation (e.g. Ω(1), Ω(n), Ω(n^2), Ω(log n), etc.)
1. Big Theta notation (e.g. Θ(1), Θ(n), Θ(n^2), Θ(log n), etc.)
1. Space complexity of algorithms
1. Comparison of time/space complexity of different algorithms
1. Asymptotic analysis of recursive algorithms
1. Amortized analysis of data structures (e.g. dynamic arrays, binary heaps, etc.)
1. Master Theorem and its application
1. Recurrence relations and solving them using recursion tree method, substitution method, and iteration method.

---

## Theory

Asymptotic notation is a mathematical notation used to describe the behavior of an algorithm's running time as the input size grows without bound. It provides a way to express the growth of an algorithm's running time in a simplified manner, independent of the specific details of the input.

There are two main types of asymptotic notation:

1. **Big O Notation**: It is used to describe the upper bound of an algorithm's running time. It describes the worst-case scenario of an algorithm. The notation is written as O(f(n)), where f(n) is a function representing the running time of the algorithm. For example, O(n) means that the running time of the algorithm is at most linear in the size of the input.

1. **Big Omega Notation**: It is used to describe the lower bound of an algorithm's running time. It describes the best-case scenario of an algorithm. The notation is written as Ω(f(n)), where f(n) is a function representing the running time of the algorithm. For example, Ω(n) means that the running time of the algorithm is at least linear in the size of the input.

1. **Big Theta Notation**: It is used to describe the average running time of an algorithm. It is a combination of both Big O and Big Omega notation. The notation is written as Θ(f(n)), where f(n) is a function representing the running time of the algorithm. For example, Θ(n) means that the running time of the algorithm is linear in the size of the input, regardless of the input.

Here is an example to illustrate how these notations work:

    Consider an algorithm that takes an array of size n as input and finds
    the maximum element in the array.

- The worst-case scenario of this algorithm is that the maximum element is at the end of the array. In this case, the algorithm needs to compare all the elements of the array, which takes O(n) time. Therefore, the running time of the algorithm in the worst-case scenario is O(n).

- The best-case scenario of this algorithm is that the maximum element is at the beginning of the array. In this case, the algorithm only needs to compare the first element of the array, which takes O(1) time. Therefore, the running time of the algorithm in the best-case scenario is Ω(1).

- On average, the algorithm needs to compare n/2 elements of the array, which takes Θ(n/2) time. Therefore, the average running time of the algorithm is Θ(n).

It is important to note that when comparing the running time of different algorithms, we only compare the dominant term of their running time. For example, if the running time of an algorithm is O(n^2) and the running time of another algorithm is O(n log n) then the second algorithm is considered as faster than the first one.

Asymptotic notation is a powerful tool to understand the performance of an algorithm and to compare the performance of different algorithms in a simplified manner. It gives an idea of how the algorithm will behave as the input size increases, without considering the specific details of the input.

---

**Space Complexity**

Space complexity refers to the amount of memory used by an algorithm during its execution. It is a measure of how much additional memory an algorithm requires as the size of the input data increases.

There are two types of space complexity:

Auxiliary Space: The extra space or temporary space used by the algorithm.
Space complexity: It is total space taken by the algorithm including Auxiliary Space and space used for input.
Auxiliary space is the temporary space used by an algorithm, for example, the space used by variables and data structures. In the case of bubble sort, the algorithm only uses a constant amount of auxiliary space, as it only requires a few variables such as "i" and "j" in the for loops, and a variable "n" to store the length of the input array. So, the auxiliary space complexity of bubble sort is O(1).

The second type of space complexity is the total space taken by an algorithm, including the space used for input. In the case of the bubble sort, the input array is modified in-place, so no additional space is required to store the sorted array. So the total space complexity of bubble sort is O(1).

Here is an example of the space complexity of a function that uses an additional data structure:

    def func(n):
        result = []
        for i in range(n):
            result.append(i)
        return result

- In this example, the function creates an empty list called "result" and then uses a for loop to append "n" elements to the list. The space complexity of this function is O(n) because the amount of memory used increases linearly with the size of the input "n".

- In general, it's important to consider both time and space complexity when analyzing and comparing algorithms, as a highly efficient algorithm in terms of time complexity may not be suitable for a particular problem if it requires too much memory.

---

Another example with explanation:

    def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

    arr = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(arr))

Explanation:

- This code defines a function called "bubble_sort" that takes an array as an input, and sorts the elements of the array in ascending order using the bubble sort algorithm.

- The bubble sort algorithm repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

- The function first initializes a variable "n" with the length of the input array. Then, it uses two nested for loops. The outer loop runs for "n" iterations, and the inner loop runs from 0 to "n-i-1".

- The inner loop compares the current element (arr[j]) with the next element (arr[j+1]). If the current element is greater than the next element, the two elements are swapped using the Pythonic "tuple swapping" method.

- This process of comparing and swapping adjacent elements continues until the inner loop completes its execution. Once the inner loop completes execution, the largest element in the array "bubbles" to the last position of the array. This is why it's called a bubble sort.

- This process is repeated for "n" iterations until all elements are in their correct positions. The function then returns the sorted array.

- In the example provided, the unsorted array [64, 34, 25, 12, 22, 11, 90] is passed to the function as an argument, and the function returns the sorted array [11, 12, 22, 25, 34, 64, 90].

- The Time complexity of bubble sort algorithm is O(n^2) in worst and average case. It has O(n) best-case performance when the input array is already sorted.

- The space complexity of bubble sort is O(1) as no extra space required.