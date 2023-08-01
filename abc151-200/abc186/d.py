# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
sortedA = sorted(A, reverse=True)

sumA = []
sum = 0
for i in range(N):
    sum += sortedA[i]
    sumA.append(sum)

ans = 0
for i in range(N-1):
    ans += (sumA[N-i-2] - (N-i-1) * sortedA[N-i-1])

print(ans)