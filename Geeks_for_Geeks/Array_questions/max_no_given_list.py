#!/usr/bin/env python3
def main(args):
    x = [1, 34, 3, 98, 9, 76, 45, 4]
    y = [str(i) for i in x]
    y.sort(reverse=True)
    res = ''.join(y)
    print(res)


def res(a):
    return


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
