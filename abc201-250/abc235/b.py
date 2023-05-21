# -*- coding: utf-8 -*-
N = int(input())
H = list(map(int, input().split()))

prev = 0
for i in range(N):
    if H[i] > prev:
        prev = H[i]
    else:
        print(prev)
        exit(0)

print(prev)