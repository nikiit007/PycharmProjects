#!/usr/bin/env python3
def main(args):
    a = [i for i in range(21, 53)]

    # a.append(31)
    print(a)
    print(len(a))
    res = 0
    for i in a:
        res = res or i
    print(res)


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
