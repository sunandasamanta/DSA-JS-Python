"""A linked list is a linear collection of data elements, called nodes, each pointing to the next node by means of a pointer. It is a dynamic data structure, as opposed to an array, which has a fixed size. The elements in a linked list are not stored in contiguous memory locations, instead, each element is a separate object with a data part and a reference (link) to the next element."""

"""Here is an example of a singly linked list in Python:"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)
    llist.insertAfter(llist.head.next, 8)
    print("Created Linked List: ")
    llist.printList()
"""In this example, the Node class is defined with two attributes: data and next. The LinkedList class contains a reference to the first node, called the head. The class has several methods for adding and deleting elements from the linked list, including push, insertAfter, append and printList. The push method adds a new node at the beginning of the list, the insertAfter method adds a new node after a given node, the append method adds a new node at the end of the list, and the printList method prints the elements of the list. The linked list is created in the __main__ block, where elements are added and the final linked list is printed out."""