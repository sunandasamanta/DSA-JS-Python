class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, value):
        self.top += 1
        self.stack.append(value)
        print("Value successfully inserted!")
        
    def pop(self):
        if self.top == -1:
            print("Error: Stack is empty!")
            return
        self.top -= 1
        print("Value successfully removed!")
        
    def peek(self):
        if self.top == -1:
            print("Error: Stack is empty!")
            return
        print("Top element is:", self.stack[self.top])
        
    def display(self):
        if self.top == -1:
            print("Error: Stack is empty!")
            return
        print("Stack elements:", self.stack)
        
    def is_empty(self):
        return self.top == -1

stack = Stack()
while True:
    print("1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter value to push: "))
        stack.push(value)
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
