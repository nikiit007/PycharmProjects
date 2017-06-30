#!/usr/bin/env python3
class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.currentnode = None

    def addnode(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.currentnode
        self.currentnode = new_node

    def reverse(self):
        prev = None
        current = self.currentnode
        while current is not None:
            LinkedList.printdata(prev, current, current.next)
            current.next, prev, current = prev, current, current.next
        self.currentnode = prev

    def detect_loop(self):
        slow = fast = self.currentnode
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def printdata(a, b, c):
        outa = a.data if a else "null"
        outb = b.data if b else "null"
        outc = c.data if c else "null"
        print(outa, outb, outc)


def findmiddle(head):
    fast = head
    slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def printll(head):
    x = []
    while head:
        x.append(head.data)
        head = head.next
    print(x)


def intersection(x, y):
    if x is None or y is None:
        return
    if x.data > y.data:
        return intersection(x.next, y)
    elif x.data < y.data:
        return intersection(x, y.next)
    temp = Node()
    temp.data = x.data
    temp.next = intersection(x.next, y.next)
    return temp


def union(x, y):
    if x is None:
        return y
    if y is None:
        return x
    temp = Node()
    if x.data > y.data:
        temp.data = x.data
        temp.next = union(x.next, y)
        return temp
    elif x.data < y.data:
        temp.data = y.data
        temp.next = union(x, y.next)
        return temp
    else:
        temp.data = x.data
        temp.next = union(x.next, y.next)
        return temp


def recursive_reverse(node):
    if node is None:
        return
    first = node
    rest = node.next

    if rest is None:
        return first

    rest = recursive_reverse(rest)
    # first.next.next = first
    first.next.next = first
    first.next = None

    return rest


def del_node(node):
    print("received the value {}".format(node.data))
    if node.next is None:
        node = None
    else:
        node.data = node.next.data
        node.next = node.next.next
    return


def insert_sorted(node, data):
    newnode = Node()
    if data >= node.data:
        newnode.data = data
        newnode.next = node
        node = newnode

    elif node.next is None:
        node.next = Node()
        node.next.data = data

    else:
        node.next = insert_sorted(node.next, data)
    return node


def main(args):
    x = LinkedList()
    y = LinkedList()
    # a = LinkedList()
    #
    # tlist = [12, 15, 10, 11, 5, 6, 2, 3]
    # print(tlist)
    #
    # for i in tlist[::-1]:
    #     a.addnode(i)
    # printll(a.currentnode)
    # z = a.currentnode

    x.addnode(1)
    x.addnode(2)
    x.addnode(3)
    x.addnode(4)
    x.addnode(5)

    y.addnode(1)
    y.addnode(3)
    y.addnode(5)
    y.addnode(7)
    y.addnode(9)
    print("making random")

    # printll(x.currentnode)
    # print("***")
    # printll(y.currentnode)
    # print("***")
    z = y.currentnode
    printll(z)
    # z = insert_sorted(z, 0)
    # print("***")
    # printll(z)
    # print('***')
    z = recursive_reverse(z)
    printll(z)



    # z = intersection(x.currentnode, y.currentnode)
    # printll(z)
    # z = union(x.currentnode, y.currentnode)
    # printll(z)

    # x.currentnode.next.next.next = x.currentnode
    # print(x.detect_loop())


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
