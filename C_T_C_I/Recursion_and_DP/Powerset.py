#!/usr/bin/env python3
def main(args):
    a = [1, 2, 3, 4]
    ps = [[]]
    for i in a:
        cs = copy.deepcopy(ps)
        k = len(cs)
        for j in range(k):
            cs[j].append(i)
        ps.extend(cs)
    for i in ps:
        print(i)


if __name__ == '__main__':
    import sys
    import copy

    sys.exit(main(sys.argv))
