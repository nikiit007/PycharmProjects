#!/usr/bin/env python3
def main(args):
    t = int(input())
    while t > 0:
        u, v = map(int, input().split())
        print(rank(u + v) + u)
        t -= 1


def rank(x):
    return 1 + (x * (x + 1)) // 2


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))

