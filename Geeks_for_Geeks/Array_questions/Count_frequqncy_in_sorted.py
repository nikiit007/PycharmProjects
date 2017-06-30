#!/usr/bin/env python3

def main(args):
    A = [2, 2, 3, 3, 4, 4, 4, 4, 4, 5]
    B = set(A)

    for i in B:
        print("first index of {} = {}".format(i, bin_search_first(A, i, 0, len(A))))
        print("last index of {} = {}".format(i, bin_search_last(A, i, 0, len(A))))


def bin_search_first(A, element, start, end):
    # print(element, start, end)
    if start > end:
        return
    if start == end or ((end - start) == 1 and A[end] != A[start]):
        return end
    mid = (start + end) // 2
    if element <= A[mid]:
        return bin_search_first(A, element, start, mid)
    else:
        return bin_search_first(A, element, mid, end)


def bin_search_last(A, element, start, end):
    # print(element, start, end)
    if start > end:
        return
    if start == end or (end - start) == 1:
        return start
    mid = (start + end) // 2
    if element < A[mid]:
        return bin_search_last(A, element, start, mid)
    else:
        return bin_search_last(A, element, mid, end)


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
