# -*- coding: utf-8 -*-
n,k,d = map(int, input().split())
a = list(map(int, input().split()))

dp = []
for i in range(n+1):
    jj = []
    for j in range(k+2):
        rr = []
        for r in range(d):
            rr.append(-1)
        jj.append(rr)
    dp.append(jj)

dp[0][0][0] = 0

for i in range(n):
    ni = i+1
    for j in range(k+1):
        for r in range(d):
            now = dp[i][j][r]
            if now == -1:
                continue
            # use
            nj = j+1
            nr = (r+a[i]) % d
            dp[ni][nj][nr] = max(dp[ni][nj][nr], now+a[i])
            # not use
            dp[ni][j][r] = max(dp[ni][j][r], now)

print(dp[n][k][0])
