# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

sortedA = sorted(A)

prev = -1
for i in range(N):
    if prev != -1 and sortedA[i] - prev != 1:
        print(sortedA[i]-1)
        break
    prev = sortedA[i]