
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

## Theory

Asymptotic notation is a mathematical notation used to describe the behavior of an algorithm's running time as the input size grows without bound. It provides a way to express the growth of an algorithm's running time in a simplified manner, independent of the specific details of the input.

There are three main types of asymptotic notation:

1. **Big O Notation**: It is used to describe the upper bound of an algorithm's running time. It describes the worst-case scenario of an algorithm. The notation is written as O(f(n)), where f(n) is a function representing the running time of the algorithm. For example, O(n) means that the running time of the algorithm is at most linear in the size of the input.

1. **Big Omega Notation**: It is used to describe the lower bound of an algorithm's running time. It describes the best-case scenario of an algorithm. The notation is written as Ω(f(n)), where f(n) is a function representing the running time of the algorithm. For example, Ω(n) means that the running time of the algorithm is at least linear in the size of the input.

1. **Big Theta Notation**: It is used to describe the average running time of an algorithm. It is a combination of both Big O and Big Omega notation. The notation is written as Θ(f(n)), where f(n) is a function representing the running time of the algorithm. For example, Θ(n) means that the running time of the algorithm is linear in the size of the input, regardless of the input.

Here is an example to illustrate how these notations work:

    Consider an algorithm that takes an array of size n as input and finds\
    the maximum element in the array.

- The worst-case scenario of this algorithm is that the maximum element is at the end of the array. In this case, the algorithm needs to compare all the elements of the array, which takes O(n) time. Therefore, the running time of the algorithm in the worst-case scenario is O(n).

- The best-case scenario of this algorithm is that the maximum element is at the beginning of the array. In this case, the algorithm only needs to compare the first element of the array, which takes O(1) time. Therefore, the running time of the algorithm in the best-case scenario is Ω(1).

- On average, the algorithm needs to compare n/2 elements of the array, which takes Θ(n/2) time. Therefore, the average running time of the algorithm is Θ(n).

It is important to note that when comparing the running time of different algorithms, we only compare the dominant term of their running time. For example, if the running time of an algorithm is O(n^2) and the running time of another algorithm is O(n log n) then the second algorithm is considered as faster than the first one.

Asymptotic notation is a powerful tool to understand the performance of an algorithm and to compare the performance of different algorithms in a simplified manner. It gives an idea of how the algorithm will behave as the input size increases, without considering the specific details of the input.

<!-- twenty five asymptotic notation questions on different algorithms, include easy, mid and difficult all -->
## Asymptotic Notation Questions

- Determine the asymptotic notation for the following algorithms:
    - Linear search
    - Binary search
    - Bubble sort
    - insertion sort
    - quick sort
    - merge sort
    - binary tree traversal
    - Dijkstra's shortest path algorithm
    - Depth-first search
    - Breadth-first search
    - Bellman-Ford algorithm
- Compare the time complexity of different sorting algorithms
- Compare the space complexity of different sorting algorithms
- Analyze the time complexity of a recursive function
- Analyze the space complexity of a recursive function
- Explain the difference between O(n) and Θ(n) notation
- Explain the difference between O(n) and Ω(n) notation
- Explain the difference between O(n log n) and Θ(n log n) notation
- What is the time complexity of an algorithm that runs in O(1) and why?
- What is the time complexity of an algorithm that runs in O(n) and why?
- What is the time complexity of an algorithm that runs in O(n^2) and why?
- What is the time complexity of an algorithm that runs in O(log n) and why?
- What is the time complexity of an algorithm that runs in O(n log n) and why?
- What is the time complexity of an algorithm that runs in O(2^n) and why?
- What is the time complexity of an algorithm that runs in O(n!) and why?
- Explain the concept of space complexity and its importance
- What is the space complexity of an algorithm that runs in O(1) and why?
- What is the space complexity of an algorithm that runs in O(n) and why?
- What is the space complexity of an algorithm that runs in O(n^2) and why?
- What is the space complexity of an algorithm that runs in O(log n) and why?
- What is the space complexity of an algorithm that runs in O(n log n) and why?
- What is the space complexity of an algorithm that runs in O(2^n) and why?

<!-- ## Twenty-Five Asymptotic Notation Questions -->