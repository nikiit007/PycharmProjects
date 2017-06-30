#!/usr/bin/env python3

def main(args):
    t = int(input())
    while t > 0:
        n = int(input())
        a = [int(i) for i in input().split()]
        a.sort(reverse=True)
        print(calc(a, n))
        t -= 1


def calc(a, n):
    max_p = 0
    sum_p = 0
    for i in range(n):
        sum_p += a[i]
        prod = (i + 1) * sum_p
        if prod >= max_p:
            max_p = prod
        else:
            return max_p + sum(a[i:])
    return max_p


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
