# -*- coding: utf-8 -*-
N = int(input())
AB = []
for i in range(N):
    a,b = map(int, input().split())
    AB.append((a,b))

dp = [[0,0]  for _ in range(N)]
dp[0] = (1,1)
mod = 998244353
for i in range(1,N):
    (prea, preb) = AB[i-1]
    (a,b) = AB[i]
    if prea != a:
        dp[i][0] += dp[i-1][0]
    if prea != b:
        dp[i][1] += dp[i-1][0]
    if preb != a:
        dp[i][0] += dp[i-1][1]
    if preb != b:
        dp[i][1] += dp[i-1][1]
    dp[i][0] %= mod
    dp[i][1] %= mod

print((dp[N-1][0]+dp[N-1][1])%mod)