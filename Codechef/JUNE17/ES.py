#!/usr/bin/env python3
import math
from decimal import Decimal


def main(args):
    n = int(input())
    e = 2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919
    val = S(e, n)
    print(math.floor(val))


def S(a, n):
    if n == 0:
        return 0
    elif n == 1:
        return math.floor(a)
    elif a >= 2:
        subt = math.floor(a) - 1
        b = a - subt
        return S(b, n) + subt * n * (n + 1) * Decimal(0.5)
    elif a > 1:
        binv = 1 - 1 / a
        b = 1 / binv
        n_ = math.floor((a - 1) * n)
        return (n + n_) * (n + n_ + 1) * Decimal(0.5) - S(b, n_)
    else:
        print("received negative value")


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
