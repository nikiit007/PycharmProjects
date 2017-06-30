#!/usr/bin/env python3
def main(args):
    a = [12, 11, 10, 5, 6, 2, 30]
    b = [1, 2, 3, 4]
    c = [4, 3, 2, 1]

    res(a)
    res(b)
    res(c)



def res(a):
    n = len(a)
    minarr = [0] * n
    maxarr = [0] * n
    minindex = 0
    maxindex = n - 1
    for i in range(n):
        if a[minindex] < a[i]:
            minarr[i] = minindex
        else:
            minarr[i] = -1
            minindex = i

    for i in range(n - 1, -1, -1):
        if a[maxindex] > a[i]:
            maxarr[i] = maxindex
        else:
            maxarr[i] = -1
            maxindex = i
    # print(a)
    # print(minarr)
    # print(maxarr)
    for i in range(n):
        if minarr[i] != -1 and maxarr[i] != -1:
            print(a[minarr[i]], a[i], a[maxarr[i]])
            return
    print("no triplet found")
    return


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
