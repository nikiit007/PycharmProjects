#!/usr/bin/env python3
class Box:
    def __init__(self, w, h, d):
        self.width = w
        self.height = h
        self.depth = d

    def __repr__(self):
        return repr((self.width, self.height, self.depth))


def longest_increasing_subsequence(boxes):
    n = len(boxes)
    lis = [boxes[i].height for i in range(n)]
    for i in range(1, n):
        for j in range(0, i):
            if boxes[i].height>boxes[j].height and boxes[i].width>boxes[j].width and lis[i]<lis[j]+boxes[i].height:
                lis[i] = lis[j] + boxes[i].height
    return max(lis)


def main(args):
    boxes = []
    for i in range(200):
        w, h, d = list(map(int, input().split(',')))
        boxes.append(Box(w, h, d))
    sorted_boxes = sorted(boxes, key=lambda box: box.depth)
    print(longest_increasing_subsequence(sorted_boxes))


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
