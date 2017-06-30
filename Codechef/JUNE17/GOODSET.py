#!/usr/bin/env python3

def main(args):
    l = [i for i in range(500, 400, -1)]
    T = int(input())
    while T > 0:
        n = int(input())
        print(*l[:n])
        T -= 1


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
