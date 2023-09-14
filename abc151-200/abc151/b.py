# -*- coding: utf-8 -*-
N,K,M = map(int, input().split())
A = list(map(int, input().split()))

sumA = 0
for i in range(N-1):
    sumA += A[i]

if sumA >= N*M:
    print("0")
else:
    zan = N*M-sumA
    if zan <= K:
        print(zan)
    else:
        print(-1)

    