#!/usr/bin/env python3
def main(args):
    stack1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    stack2 = []
    stack3 = []

    print("stack1 is", stack1)
    print("stack2 is", stack2)
    print("stack3 is", stack3)

    hanoi(stack1, stack2, stack3)
    print("stack1 is", stack1)
    print("stack2 is", stack2)
    print("stack3 is", stack3)
    return 0


def hanoi(stack1, stack2, stack3):
    if len(stack1) == 0 and len(stack2) == 0:
        return
    elif len(stack1) == 1:
        stack3.append(stack1.pop())
    elif len(stack1) == 2:
        stack2.append(stack1.pop())
        stack3.append(stack1.pop())
        stack3.append(stack2.pop())
    else:
        stack2.append(stack1.pop())
        hanoi(stack1, stack2, stack3)
        stack3.append(stack2.pop())


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
