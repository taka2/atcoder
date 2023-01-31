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
    # ゴールからたどる
    ans = []
    currentSum = S
    for currentPos in range(N, 0, -1):
        if dp[currentPos-1][currentSum] != 1:
            ans.append(currentPos)
            currentSum -= A[currentPos]
    ans.reverse()
    print(*ans)
 
else:
    print("-1")