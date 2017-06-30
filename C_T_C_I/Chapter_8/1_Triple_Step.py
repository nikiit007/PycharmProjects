#!/usr/bin/env python3
def triplesteps(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return triplesteps(n - 1) + triplesteps(n - 2) + triplesteps(n - 3)


def main(args):
    for i in range(10):
        print(i, triplesteps(i))
    n = 10
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1 + dp[1]

    for i in range(3, n):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    for i in range(10):
        print(i, dp[i])


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))
