#!/usr/bin/env python3

def main(args):
    A = [4, 5, 10, 11]
    print(find_missing(A, 0, len(A)))


def find_missing(A, start, end):
    if start > end:
        return end + 1
    print("start={},A[start]={}".format(start, A[start]))
    if start != A[start]:
        return start
    mid = (start + end) // 2
    if A[mid] < mid:
        return find_missing(A, start, mid)
    else:
        return find_missing(A, mid, end)


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
