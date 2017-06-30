#!/usr/bin/env python3
import heapq


class MinHeap:
    def __init__(self):
        self.data = []

    def push(self, val):
        heapq.heappush(self.data, val)

    def pop(self):
        return heapq.heappop(self.data)

    def top(self):
        return self.data[0]

    def size(self):
        return len(self.data)


class MaxHeap:
    def __init__(self):
        self.data = []

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)

    def top(self):
        return -self.data[0]

    def size(self):
        return len(self.data)


def main(args):
    min_h = MinHeap()
    max_h = MaxHeap()
    A = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    median = A[0]
    print("element_entered={}".format(A[0]))
    print("minheap={}".format(min_h.data))
    print("maxheap={}".format(print_proper(max_h.data)))
    print("median={}".format(median))
    print("")
    median = (A[0] + A[1]) / 2

    if A[0] < median:
        max_h.push(A[0])
        min_h.push(A[1])
    else:
        min_h.push(A[0])
        max_h.push(A[1])
    print("element_entered={}".format(A[1]))
    print("minheap={}".format(min_h.data))
    print("maxheap={}".format(print_proper(max_h.data)))
    print("median={}".format(median))
    print("")
    for i in range(2, len(A)):
        if A[i] < median:
            max_h.push(A[i])
        else:
            min_h.push(A[i])
        if min_h.size() > (max_h.size() + 1):
            max_h.push(min_h.pop())
        elif max_h.size() > (min_h.size() + 1):
            min_h.push(max_h.pop())
        if min_h.size() > max_h.size():
            median = min_h.top()
        elif min_h.size() < max_h.size():
            median = max_h.top()
        else:
            median = (min_h.top() + max_h.top()) / 2
        print("element_entered={}".format(A[i]))
        print("minheap={}".format(min_h.data))
        print("maxheap={}".format(print_proper(max_h.data)))
        print("median={}".format(median))
        print("")


def print_proper(x):
    temp = []
    for i in x:
        temp.append(abs(i))
    return temp


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
