#!/usr/bin/env python3



def main(args):
    a = [0, 1, 0, 2, 0, 0, 1, 2, 2, 2, 2, 0, 0, 1, 1, 1, 1]
    dutch_flag_3(a)
    print(a)


def dutch_flag_2(a):
    n = len(a)
    low = 0
    high = n - 1
    while low <= high:
        if a[low] == 0:
            low += 1
        else:
            a[low], a[high] = a[high], a[low]
            high -= 1


def dutch_flag_3(a):
    n = len(a)
    low = mid = 0
    high = n - 1
    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            mid += 1
            low += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
