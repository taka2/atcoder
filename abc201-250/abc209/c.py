# -*- coding: utf-8 -*-
N = int(input())
C = list(map(int, input().split()))

sortedC = sorted(C)

ans = 1
for i in range(N):
    ans *= (sortedC[i] - i)
    ans %= (10**9 + 7)

print(ans)