# -*- coding: utf-8 -*-
N,W = map(int, input().split())
A = [(0,0)]
for i in range(N):
    w,v = map(int, input().split())
    A.append((w,v))

dp = [[0] * (100000+1) for i in range(N+1)]

# 1行目のdp配列初期化
dp[0][0] = 0
for i in range(1, 100000+1):
    dp[0][i] = 99999999999999999999

for i in range(1,N+1):
    (w,v) = A[i]
    for j in range(100000+1):
        dp[i][j] = min(dp[i-1][j], dp[i-1][j-v]+w)

ans = 0
for i in range(100000+1):
    if dp[N][i] <= W:
        ans = i
print(ans)