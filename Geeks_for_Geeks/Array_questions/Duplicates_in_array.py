#!/usr/bin/env python3
def main(args):
    arr = [0, 1, 2, 3, 1, 3, 6, 6, 0, 0, 8, 8]
    print(arr)
    print(dup_chk(arr))


def dup_chk(arr):
    result = []
    n = len(arr)
    print(n)
    for i in arr:
        arr[i % n] += n
    print(arr)
    arr = [i //n for i in arr]
    print(arr)
    for i in range(n):
        if arr[i] > 1:
            result.append(i)
    return result


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
