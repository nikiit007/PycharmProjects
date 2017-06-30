#!/usr/bin/env python3
def main(args):
    x = LinkedList()
    k = 1
    while k < 15:
        x.addNode(k)
        k += 1

    head = x.current_node
    print(head.data)
    print(head.next.data)
    # printkthtolast(head, 7)
    return 0


# recursive implementation
def printkthtolast(head, k):
    if head is None:
        return 0
    index = printkthtolast(head.next, k) + 1
    if index == k:
        print("kth element below")
        print(head.data)
    print(index)
    return index


class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.current_node = None

    def addNode(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.current_node
        self.current_node = new_node


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
