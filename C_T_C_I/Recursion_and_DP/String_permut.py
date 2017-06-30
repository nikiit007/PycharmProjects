#!/usr/bin/env python3
def main(args):
    orig_str = "caa"
    a = list(orig_str)
    n = len(a)
    p = []
    permut(a, 0, n - 1, p)
    for i in p:
        print(i)


def permut(a, l, r, p):
    if l == r:
        p.append(''.join(a))

    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permut(a, l + 1, r, p)
            a[l], a[i] = a[i], a[l]


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
