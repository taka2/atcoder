# -*- coding: utf-8 -*-
N = int(input())
L = list(map(int, input().split()))

sortedL = sorted(L)
maxL = sortedL[N-1]
sumL = 0
for i in range(N-1):
    sumL += sortedL[i]

if maxL < sumL:
    print("Yes")
else:
    print("No")