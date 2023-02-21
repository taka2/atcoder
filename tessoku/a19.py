# -*- coding: utf-8 -*-
N,W = map(int, input().split())
A = [(0,0)]
for i in range(N):
    w,v = map(int, input().split())
    A.append((w,v))
 
dp = [[0] * (W+1) for i in range(N+1)]
 
# 1行目のdp配列初期化
dp[0][0] = 0
 
for i in range(1,N+1):
    (w,v) = A[i]
    for j in range(W+1):
        if j < w:
            # 対象の品物の重さが達していない場合は、前の結果をそのままコピー
            dp[i][j] = dp[i-1][j]
        else:
            # 前の結果と、今回の結果のうち、価値が大きい方を採用する
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
 
ans = 0
for i in range(W+1):
    ans = max(ans, dp[N][i])
print(ans)