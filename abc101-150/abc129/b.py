# -*- coding: utf-8 -*-
N = int(input())
W = list(map(int, input().split()))

ans = 99999
for i in range(N-1):
    leftSum = 0
    rightSum = 0
    for j in range(i+1):
        leftSum += W[j]
    for k in range(i+1, N):
        rightSum += W[k]
    ans = min(ans, abs(leftSum-rightSum))

print(ans)