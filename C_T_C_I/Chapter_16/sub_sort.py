#!/usr/bin/env python3

def main(args):
    arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    i = 0
    left = arr[0]
    while arr[i] >= left:
        left = arr[i]
        i += 1
    l = i

    i = len(arr) - 1
    right = arr[i]
    while arr[i] <= right:
        right = arr[i]
        i -= 1
    r = i
    print("left=", left)
    print("right=", right)
    print(arr[l])
    print(arr[r])

    min_arr = min(arr[l: r + 1] + [right])
    max_arr = max(arr[l: r + 1] + [left])

    print(min_arr, max_arr)


    i = l - 1
    while arr[i] > min_arr:
        i -= 1
    m = i+1

    i = r + 1
    while arr[i] < max_arr:
        i += 1
    n = i-1

    print(m, n)


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
