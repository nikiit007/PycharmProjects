#!/usr/bin/env python3
import copy


def main(args):
    t = int(input())
    while t > 0:
        n, k = input().split()
        n, k = int(n), int(k)
        wholeset = set(i for i in range(1, k + 1))
        # print("wholeset is= ", wholeset)
        a = [[] for i in range(n)]
        for i in range(n):
            input_stream = input().split()
            a[i] = set(map(int, input_stream[1:]))
        c = 0
        for i in range(n):
            diffset = wholeset - a[i]
            # print("for {} diffeset is {}".format(a[i], diffset))
            for j in range(i + 1, n):
                if find_set(diffset, a[j]):
                    c += 1
        print(c)
        t -= 1


def find_set(set1, set2):
    for i in set1:
        if i not in set2:
            return False
    return True


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
