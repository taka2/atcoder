# -*- coding: utf-8 -*-
from collections import defaultdict

N = int(input())
A = [0] * 2 + list(map(int, input().split()))

G = defaultdict(list)
for i in range(2, N+1):
    G[A[i]].append(i)

dp = [0] * (N+1)

for i in range(N, 0, -1):
    for buka in G[i]:
        dp[i] += dp[buka] + 1

ans = []
for i in range(1, N+1):
    ans.append(dp[i])

print(*ans)