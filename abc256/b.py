# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int, input().split()))

p = 0
c = 0
for i in range(n):
    c += 1
    c = c << a[i]
    if c >= 128:
        p += 1
        c -= 128
    if c >= 64:
        p += 1
        c -= 64
    if c >= 32:
        p += 1
        c -= 32
    if c >= 16:
        p += 1
        c -= 16

print(p)