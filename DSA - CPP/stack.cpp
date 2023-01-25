#include <iostream>
using namespace std;

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
	// stack.push(1);
	// stack.push(2);
	// stack.push(3);
	// stack.display();
	// stack.pop();
	// stack.display();
	// stack.pop();
	// stack.display();

		int user_input;
	while (true)
	{
		cout << "Enter 1 to Push Element, 2 to Delete, 3 to Display, 4 to see the top and 5 to exit: ";
		scanf("%d", &user_input);
		switch (user_input)
		{
		case 1:
			stack.push(1);
			stack.push(2);
			stack.push(3);
			stack.push(4);
			stack.push(5);
			stack.push(6);
		case 2:
			stack.pop();
		case 3:
			stack.display();
		default:
			break;
		}

		if (user_input >= 5 or user_input < 1)
		{
			break;
		}
		

	}
		

	return 0;
}