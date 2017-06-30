#!/usr/bin/env python3
def main(args):
    s = [1, 5, 10,25]
    n = 30
    print(coin_change(s, n))


def cc(s, n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m <= 0:
        return 0
    else:
        return cc(s, n, m - 1) + cc(s, n - s[m - 1], m)


def coin_change(s, n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in s:
        for j in range(i, n + 1):
            dp[j] += dp[j-i]

    print(dp)
    


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
