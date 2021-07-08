from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self,):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    s = Stack()
    s.push(10)
    print(s.is_empty())
    print(s.peek())
    print(s.is_empty())
    print(s.pop())
    print(s.is_empty())

