#!/usr/bin/env python3
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def main(args):
    a = [13, 7, 6, 12]
    print(nge(a))


def nge(a):
    s = Stack()
    res = []
    for i in a:
        if s.isEmpty():
            s.push(i)
        else:
            while not s.isEmpty() and i > s.peek():
                res.append((s.pop(), i))
            s.push(i)
    while not s.isEmpty():
        res.append((s.pop(), -1))
    return res


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
