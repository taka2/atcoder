# -*- coding: utf-8 -*-
N = int(input())
H = list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = 0
dp[2] = abs(H[0]-H[1])
for i in range(3,N+1):
    dp[i] = min(dp[i-1]+abs(H[i-1]-H[i-2]), dp[i-2]+abs(H[i-1]-H[i-3]))

print(dp[N])