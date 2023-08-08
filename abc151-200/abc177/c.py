# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

mod = 10**9+7
sumA = []
sum = 0
for i in range(N):
    sum += A[i]
    sumA.append(sum)

ans = 0
for i in range(N):
    sum -= A[i]
    if sum < 0:
        sum += mod

    ans += A[i] * sum
    ans %= mod

print(ans)