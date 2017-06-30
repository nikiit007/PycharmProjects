#!/usr/bin/env python3

def main(args):
    A = [1, 2, 3, 6]
    B = [4, 6, 8, 10]
    print(calc_median(A, B))


def calc_median(A, B):
    print(A, B)
    n=len(A)
    if len(A) == 1 and len(B) == 1:
        return (A[0] + B[0]) / 2
    if len(A) == 2 and len(B) == 2:
        return (max(A[0], B[0]) + min(A[1], B[1])) / 2
    i1, m1 = median(A)
    i2, m2 = median(B)
    print(i1, m1)
    print(i2, m2)

    if m1 == m2:
        return m1

    if m1 < m2:
        print("{} is less than {}".format(m1, m2))
        if n % 2 == 1:
            med = calc_median(A[i1:], B[:i2 + 1])
        else:
            med = calc_median(A[i1:], B[:i2])
        return med
    else:
        print("{} is greater than {}".format(m1, m2))
        if n % 2 == 1:
            med = calc_median(A[:i1 + 1], B[i2:])
        else:
            med = calc_median(A[:i1], B[i2:])
        return med


def median(A):
    n = len(A)
    if n % 2 == 0:
        return n // 2, (A[n // 2 - 1] + A[n // 2]) / 2
    else:
        return n // 2, A[n // 2]


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
