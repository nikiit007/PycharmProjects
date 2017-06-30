#!/usr/bin/env python3

def main(args):
    A = [2, 3, 10, 6, 4, 8, 1]
    B = [7, 9, 5, 6, 3, 2]
    C = [80, 2, 6, 3, 100]
    D = [6, 5, 4, 3, 2, 1]

    print(find_max(A))
    print(find_max(B))
    print(find_max(C))


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
        maxdiff = max(maxdiff, Rmax[j] - Lmin[i])
        j += 1
        i += 1
    return maxdiff


if __name__ == '__main__':
    import sys
    import heapq

    sys.exit(main(sys.argv))
