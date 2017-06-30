#!/usr/bin/env python3
import copy


def parens(inp, result):
    if inp == 0:
        return
    if inp == 1:
        result.append("()")
        return
    parens(inp - 1, result)
    result_copy = copy.deepcopy(result)
    for i in result_copy:
        result.append("(" + i + ")")
        result.append(i + "()")
        if ("()" + i) not in result:
            result.append("()" + i)
        result.remove(i)


def main(args):
    result = []
    parens(3, result)
    print(result)


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
