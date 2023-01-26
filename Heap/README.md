
# Heap

A heap is a special kind of tree-based data structure in which the tree is a complete binary tree. There are two types of heaps:

**Min Heap**: In a Min Heap, the value of the root node is always the minimum among all the nodes in the heap. This means that the left and right child nodes of the root node must be greater than or equal to the root node. Similarly, all the descendants of the root node must also be greater than or equal to the root node. This property is known as the heap property.

**Max Heap**: In a Max Heap, the value of the root node is always the maximum among all the nodes in the heap. This means that the left and right child nodes of the root node must be less than or equal to the root node. Similarly, all the descendants of the root node must also be less than or equal to the root node. This property is also known as the heap property.

The main difference between a min heap and a max heap is the ordering of elements based on their values. Min heap is used to find the smallest element and Max heap is used to find the largest element.

Example of a Min Heap:

         3
       /   \
      9     10
     / \    /
    20  30 15

In this example, the value of the root node is 3 which is smaller than its children 9 and 10. And the value of 9 is smaller than its children 20 and 30, and so on.

Example of a Max Heap:

      15
     /  \
    10  8
    / \
    5  2

In this example, the value of the root node is 15 which is greater than its children 10 and 8. And the value of 10 is greater than its children 5 and 2, and so on.

In both examples, the root node satisfies the heap property, where the root node is the minimum element for Min Heap and the root node is the maximum element for Max Heap.

Heaps are commonly implemented using an array or a list in which the root node is stored at index 0, the left child of a node at index i is stored at *index 2 i + 1, and the right child of a node at index i is stored at index 2 i + 2*.

Here is an example of a Python implementation of a Min Heap:

    class MinHeap:
        def __init__(self):
            self.heap = []

        def parent(self, i):
            return (i-1)//2

        def insertKey(self, k):
            self.heap.append(k)
            i = len(self.heap) - 1
            while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
                self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
                i = self.parent(i)

        def extractMin(self):
            if len(self.heap) <= 0:
                return
            if len(self.heap) == 1:
                return self.heap.pop()
            root = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.minHeapify(0)
            return root

        def minHeapify(self, i):
            l = 2 * i + 1
            r = 2 * i + 2
            smallest = i
            if l < len(self.heap) and self.heap[l] < self.heap[i]:
                smallest = l
            if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                self.minHeapify(smallest)

This is a basic implementation of a Min Heap data structure, where the insertKey method is used to insert a new key into the heap, extractMin method is used to remove and return the root node (minimum value), minHeapify is used to maintain the min-heap property after extracting the root node, and the parent function is used to get the parent index of a given index.

Applications of Heap Data Structure:

- Heap data structure is used in sorting algorithms such as Heap Sort and Selection Sort.
- Heap data structure is used in Graph algorithms such as Dijkstra's shortest path algorithm and Prim's algorithm for minimum spanning tree.
- Heap data structure is used in Priority Queue implementation.
- Heap data structure is used in implementing certain algorithms such as the Huffman coding algorithm.

Advantages of Heap Data Structure:

- Heap data structure has a time complexity of O(log n) for both insertion and deletion, making it efficient for large data sets.
- Heap data structure can be easily implemented using an array or a list, making it easy to understand and implement.
- Heap data structure is a complete binary tree, which means that it can be easily represented using an array.
- Heap data structure allows for constant-time access to the maximum or minimum element.

Disadvantages of Heap Data Structure:

- Heap data structure is not suitable for searching for a specific element as it has a time complexity of O(n) for searching.
- Heap data structure has a high overhead for maintaining the heap property as it needs to continually rearrange elements after insertion or deletion.
- Heap data structure is not suitable for small data sets as the overhead may outweigh the benefits of using it.

In conclusion, heap data structure is an efficient data structure for data sets that require priority-based access, but it is not ideal for searching and may have a high overhead for small data sets.
