#!/usr/bin/env python3
def main(args):
    a = '1'
    b = 'a'
    arr = [a, b, a, b, a, b, b, b, b, b, a, a, a, a, a, b, a, b, a, b, b, a, a, a, a, a, a, a]
    print(final_ans(arr))


def final_ans(arr):
    n = len(arr)
    hashdiff = {}
    num = [0] * n
    letters = [0] * n
    diff = [0] * n
    if arr[0] == '1':
        num[0] = 1
    else:
        letters[0] = 1
    diff[0] = num[0] - letters[0]

    for i in range(1, n):
        num[i] += num[i - 1] + (1 if arr[i] == '1' else 0)
        letters[i] += letters[i - 1] + (1 if arr[i] == 'a' else 0)
        diff[i] = num[i] - letters[i]

    diff_max = 0
    for i in range(0, n):
        if diff[i] not in hashdiff:
            hashdiff[diff[i]] = i
        else:
            if i - hashdiff[diff[i]] > diff_max:
                diff_max = i - hashdiff[diff[i]]
    print(arr)
    print(num)
    print(letters)
    print(diff)
    return diff_max


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
