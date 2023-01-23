#include <iostream>

const int MAX_SIZE = 100;

class Stack
{
private:
	int arr[MAX_SIZE];
	int top;

public:
	Stack()
	{
		top = -1;
	}
	void push(int value)
	{
		if (top == MAX_SIZE - 1)
		{
			std::cout << "Error: Stack overflow" << std::endl;
			return;
		}
		arr[++top] = value;
	}
	void pop()
	{
		if (top == -1)
		{
			std::cout << "Error: Stack underflow" << std::endl;
			return;
		}
		top--;
	}
	int peek()
	{
		if (top == -1)
		{
			std::cout << "Error: Stack is empty" << std::endl;
			return -1;
		}
		return arr[top];
	}
	bool is_empty()
	{
		return top == -1;
	}
	void display()
	{
		if (top == -1)
		{
			std::cout << "Error: Stack is empty" << std::endl;
			return;
		}
		std::cout << "Stack elements: ";
		for (int i = top; i >= 0; i--)
		{
			std::cout << arr[i] << " ";
		}
		std::cout << std::endl;
	}
};

int main()
{
	Stack stack;
	int choice, value;
	while (true)
	{
		std::cout << "1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit\n";
		std::cout << "Enter your choice: ";
		std::cin >> choice;
		switch (choice)
		{
		case 1:
			std::cout << "Enter value to push: ";
			std::cin >> value;
			stack.push(value);
			break;
		case 2:
			stack.pop();
			break;
		case 3:
			std::cout << "Top element is: " << stack.peek() << std::endl;
			break;
		case 4:
			stack.display();
			break;
		case 5:
			exit(0);
		default:
			std::cout << "Invalid choice" << std::endl;
			break;
		}
	}
	return 0;
}
