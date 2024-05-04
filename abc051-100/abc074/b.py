# -*- coding: utf-8 -*-
N = int(input())
K = int(input())
x = list(map(int, input().split()))

ans = 0
for i in range(N):
    xn = x[i]
    ans += (min(xn, abs(K-xn)) * 2)

print(ans)