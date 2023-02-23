# -*- coding: utf-8 -*-
N,X = map(int, input().split())
ab = [(0,0)]
for i in range(N):
    (a,b) = map(int, input().split())
    ab.append((a,b))

dp = [[0] * (X+101) for i in range(N+1)]

# 1行目のdp配列初期化
dp[0][0] = 1

for i in range(1,N+1):
    (a,b) = ab[i]
    for j in range(X+1):
        if dp[i-1][j] == 1:
            dp[i][j+a] = 1
            dp[i][j+b] = 1

if dp[N][X] == 1:
    print("Yes")
else:
    print("No")