# 2021-01-20
# Emma Benjaminson
# Implementation of stacks
# Source: https://medium.com/@kojinoshiba/data-structures-in-python-series-2-stacks-queues-8e2a1703d67b

class Stack:
    def __init__(self):
        self.stack = [] 

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self, val):
        return self.stack.append(val)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


if __name__ == "__main__":

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("the stack is: ")
    print(stack)
    print("peeking at the stack: ")
    print(stack.peek())
    print("stack size is: ")
    print(stack.size())
    print("is the stack empty?")
    print(stack.is_empty())

    print("pop an element and check size")
    print(stack.pop())
    print(stack.size())

