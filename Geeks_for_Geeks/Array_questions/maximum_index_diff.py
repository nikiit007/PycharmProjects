#!/usr/bin/env python3

def main(args):
    A = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    B = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
    C = [1, 2, 3, 4, 5, 6]
    D = [6, 5, 4, 3, 2, 1]

    print(find_max(A))
    print(find_max(B))
    print(find_max(C))
    print(find_max(D))


def find_max(A):
    n = len(A)
    Lmin = [0] * n
    Rmax = [0] * n

    Lmin[0] = A[0]
    Rmax[n - 1] = A[n - 1]
    for i in range(1, n):
        Lmin[i] = min(Lmin[i - 1], A[i])
    for i in range(n - 2, -1, -1):
        Rmax[i] = max(Rmax[i + 1], A[i])
    i = j = 0
    maxdiff = -1
    print(A)
    print(Lmin)
    print(Rmax)
    while i < n and j < n:
        if Lmin[i] < Rmax[j]:
            maxdiff = max(maxdiff, j - i)
            j += 1
        else:
            i += 1
    return maxdiff


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
