# -*- coding: utf-8 -*-
N,K = map(int, input().split())
H = list(map(int, input().split()))

sortedH = sorted(H, reverse=True)

sumA = 0
zanK = K
for i in range(N):
    if zanK > 0:
        zanK -= 1
    else:
        sumA += sortedH[i]

print(sumA)