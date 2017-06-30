#!/usr/bin/env python3

def main(args):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(arr)
    shufflearray(arr)
    print(arr)


def shufflearray(arr):
    n = len(arr)
    for i in range(0, n):
        k = rand(0, i)
        arr[k], arr[i] = arr[i], arr[k]


def rand(lower, higher):
    return lower + int(random.random() * (higher - lower + 1))


if __name__ == '__main__':
    import sys
    import random

    sys.exit(main(sys.argv))
