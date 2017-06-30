#!/usr/bin/env python3
def bitonic(a):
    n = len(a)
    res = 0
    left = [0] * n
    right = [0] * n
    left[0] = 1
    right[n - 1] = 1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            left[i] = left[i - 1] + 1
        else:
            left[i] = 1
    for i in range(n - 2, -1, -1):
        if a[i] > a[i + 1]:
            right[i] = right[i + 1] + 1
        else:
            right[i] = 1
    for i in range(n):
        res = max(res, left[i] + right[i] - 1)
    return res


def main(args):
    a = [12, 4, 78, 90, 45, 23]
    print(bitonic(a))


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
