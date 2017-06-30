#!/usr/bin/env python3
class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def weavelist(first, second, results, prefix):
    if len(first) == 0 or len(second) == 0:
        result = list(prefix)
        result.extend(first)
        result.extend(second)
        results.append(result)
        return

    headfirst = first.pop(0)
    prefix.append(headfirst)
    weavelist(first, second, results, prefix)
    prefix.pop()
    first.insert(0, headfirst)

    headsecond = second.pop(0)
    prefix.append(headsecond)
    weavelist(first, second, results, prefix)
    prefix.pop()
    second.insert(0, headsecond)


def allsequence(node):
    result = []
    if node is None:
        result.append([])
        return result
    prefix = []
    prefix.append(node.data)



    leftlist = allsequence(node.left)


    rightlist = allsequence(node.right)



    for l in leftlist:
        for r in rightlist:
            weave = []

            weavelist(l, r, weave, prefix)
            result.extend(weave)

    return result


def main(args):
    node = BinaryTree(100)
    node.left = BinaryTree(50)
    node.right = BinaryTree(110)
    node.left.left = BinaryTree(20)
    node.left.right = BinaryTree(75)

    node.right.right = BinaryTree(150)
    node.right.right.left = BinaryTree(120)
    node.right.right.right = BinaryTree(170)
    x = allsequence(node)
    for i in x:
        print(i)
    print(len(x))

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
