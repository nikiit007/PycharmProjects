#!/usr/bin/env python3
import bisect


def main(args):
    t = int(input())
    while t > 0:
        p, q, r = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        a.sort()
        b.sort()
        c.sort()
        a_sum = cum_sum(a, p)
        # b_sum = cum_sum(b, q)
        c_sum = cum_sum(c, r)
        sum_ = 0
        for i in b:
            p_ = bisect.bisect(a, i)
            r_ = bisect.bisect(c, i)
            if p_ > 0 and r_ > 0:
                sum_ = (sum_ + p_ * r_ * i * i + i * (r_ * a_sum[p_ - 1] + p_ * c_sum[r_ - 1]) + a_sum[p_ - 1] * c_sum[
                    r_ - 1]) % (10 ** 9 + 7)
        print(sum_)
        t -= 1


def cum_sum(arr, n):
    sum_arr = [0] * n
    sum_arr[0] = arr[0]
    for i in range(1, n):
        sum_arr[i] = sum_arr[i - 1] + arr[i]
    return sum_arr


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
