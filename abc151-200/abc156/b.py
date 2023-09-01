# -*- coding: utf-8 -*-
N,K = map(int, input().split())

ans = 0
n = N
while n > 0:
    n = n // K
    ans += 1

print(ans)