# -*- coding: utf-8 -*-
S = input()
n = len(S)

# 0で埋めた二次元配列を用意する
dp = [[0 for j in range(n+1)] for i in range(n+1)]

dp[0][0] = 1
for i in range(n):
    ch = S[i]
    for j in range(n):
        if ch != ')':
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] = dp[i+1][j+1] % 998244353
        if j != 0 and ch != '(':
            dp[i+1][j-1] += dp[i][j]
            dp[i+1][j-1] = dp[i+1][j-1] % 998244353

print(dp[n][0])