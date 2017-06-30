#!/usr/bin/env python3

def main(args):
    A = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    B = [3, 3, 4, 2, 4, 4, 2, 4]
    print(is_majority(A, maj(A)))
    print(is_majority(B, maj(B)))


def maj(A):
    e = A[0]
    c = 1
    for i in A[1:]:
        if i == e:
            c += 1
        else:
            c -= 1
        if c == 0:
            e, c = i, 1
    return e


def is_majority(A, e):
    count = 0
    for i in A:
        if i == e:
            count += 1
    if count > len(A) // 2:
        return e
    else:
        return "No Majority Element"


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
