#!/usr/bin/env python3

n, k = list(map(int, input().split()))

a = []
b = []
for i in range(0, n):
    a.append(0)

opencount = 0
for i in range(0, k):

    s = input()
    if s == 'CLOSEALL':
        b[i] = 0
    else:
        index = int(s[5:])
        if a[index] == 0:
            a[index] = 1
            opencount += 1
        else:
            a[index] = 0
            opencount -=1

    print(opencount)