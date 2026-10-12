# Stack implementation using a class and objects.
# A stack is LIFO (last in, first out): the last value pushed is the
# first value popped.


class Stack:
    def __init__(self, size):
        self.stack = [None] * size   # fixed-size array
        self.top = -1                # index of the top element; -1 = empty

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.stack) - 1

    def push(self, value):
        if self.is_full():
            print("Stack overflow: cannot push", value)
            return
        self.top = self.top + 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Stack underflow: nothing to pop")
            return None
        popped = self.stack[self.top]
        self.stack[self.top] = None
        self.top = self.top - 1
        return popped

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top]


size = int(input("Enter the size of the stack: "))
s = Stack(size)

for i in range(size):
    value = int(input("Enter a value to push: "))
    s.push(value)

print("\nThe stack is:", s.stack)
print("The top element is:", s.peek())

popped = s.pop()
print("\nPopped element:", popped)
print("After popping, the stack is:", s.stack[:s.top + 1])
print("Top of stack is:", s.peek())
