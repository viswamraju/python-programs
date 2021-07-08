from datastructures.stack_demo.stack import Stack


class Queue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, val):
        self.s1.push(val)

    def pop(self):
        # Move all elements to s2 and then do pop()
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())

        val = self.s2.pop()

        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())
        return val

    def size(self):
        return self.s1.size()

    def is_empty(self):
        return self.s1.is_empty()


if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)

    print(q.size())
    print(q.is_empty())

    print(q.pop())
    print(q.size())