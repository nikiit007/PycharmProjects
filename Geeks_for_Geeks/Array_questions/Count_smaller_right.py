#!/usr/bin/env python3
import bisect


def main(args):
    a = [12, 1, 2, 3, 0, 11, 4]
    b = [5, 4, 3, 2, 1]
    c = [1, 2, 3, 4, 5]
    d = [10, 6, 15, 20, 30, 5, 7, 5, 5, 15, 6]
    print(csmaller(a))
    print(csmaller(b))
    print(csmaller(c))
    print(csmaller(d))


def csmaller(a):
    b = []
    n = len(a)
    res = []
    for i in range(n - 1, -1, -1):
        bisect.insort_left(b, a[i])
        res.append(bisect.bisect_left(b, a[i]))
    return res[::-1]


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
