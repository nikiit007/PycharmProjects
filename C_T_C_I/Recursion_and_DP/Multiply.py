#!/usr/bin/env python3
def main(args):
    print(mult(9, 19))


def mult(small, big):
    if small > big:
        big, small = small, big
    if small == 0:
        return 0
    elif small == 1:
        return big
    else:
        s = small >> 1
        if small % 2 == 0:
            return mult(s, big) + mult(s, big)
        else:
            return mult(s, big) + mult(s, big) + big


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))

