#!/usr/bin/env python3
def main(args):
    x = [1, 0, -20, 0, 1, 2, 5, 0, 9, -9]
    print(ans(x))


def ans(a):
    maxsofar = a[0]
    minhere = a[0]
    maxhere = a[0]
    for i in range(1, len(a)):
        temp = maxhere
        maxhere = max(max(maxhere * a[i], minhere * a[i]), a[i])
        minhere = min(min(temp * a[i], minhere * a[i]), a[i])
        maxsofar = max(maxhere, maxsofar)
    return maxsofar


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
