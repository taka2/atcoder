# -*- coding: utf-8 -*-
N,S = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [[0] * (S+1) for i in range(N+1)]

# 1行目のdp配列初期化
dp[0][0] = 1

for i in range(1,N+1):
    for j in range(S+1):
        if dp[i-1][j] == 1:
            dp[i][j] = 1
            if (j+A[i]) <= S:
                dp[i][j+A[i]] = 1

if dp[N][S] == 1:
    print("Yes")
else:
    print("No")