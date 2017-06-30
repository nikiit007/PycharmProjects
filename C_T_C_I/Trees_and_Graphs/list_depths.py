#!/usr/bin/env python3
def main(args):
    bt = BinaryTree(1)
    bt.left = BinaryTree(2)
    bt.right = BinaryTree(3)
    bt.left.left = BinaryTree(4)
    bt.left.right = BinaryTree(5)
    bt.left.left.left = BinaryTree(8)
    bt.left.left.right = BinaryTree(9)
    bt.right.left = BinaryTree(6)
    bt.right.right = BinaryTree(7)
    bt.right.right.right = BinaryTree(10)
    inorder(bt)
    ll = [[] for i in range(4)]
    preorder_list_create(bt, ll, 0)
    print(ll[0])
    print(ll[1])
    print(ll[2])
    print(ll[3])
    return 0


def inorder(bt):
    if bt is None:
        return
    inorder(bt.left)
    print(bt.data)
    inorder(bt.right)


def preorder_list_create(bt, ll, level):
    if bt is None:
        return
    ll[level].append(bt.data)
    preorder_list_create(bt.left, ll, level + 1)
    preorder_list_create(bt.right, ll, level + 1)


class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
