class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print("Value successfully inserted!")
        
    def pop(self):
        if self.top is None:
            print("Error: Stack is empty!")
            return
        self.top = self.top.next
        print("Value successfully removed!")
        
    def peek(self):
        if self.top is None:
            print("Error: Stack is empty!")
            return
        print("Top element is:", self.top.data)
        
    def display(self):
        if self.top is None:
            print("Error: Stack is empty!")
            return
        current = self.top
        while current:
            print(current.data, end = ' ')
            current = current.next
        print()

stack = Stack()
while True:
    print("1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter value to push: "))
        stack.push(data)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
