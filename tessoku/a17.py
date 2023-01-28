# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
A.insert(0,0)
B = list(map(int, input().split()))
B.insert(0,0)

# DP
dp = [0] * (N+1)
dp[1] = 0
dp[2] = A[1]
for i in range(3,N+1):
    dp[i] = min(dp[i-1]+A[i-1], dp[i-2]+B[i-2])

# ゴールからたどる
ans = [N]
currentCost = dp[N]
currentPos = N
while currentPos != 1:
    a = currentCost - A[currentPos-1]
    if a == dp[currentPos-1]:
        currentCost = dp[currentPos-1]
        currentPos -= 1
        ans.append(currentPos)
        continue
    b = currentCost - B[currentPos-2]
    if b == dp[currentPos-2]:
        currentCost = dp[currentPos-2]
        currentPos -= 2
        ans.append(currentPos)

ans.reverse()
print(len(ans))
print(*ans)