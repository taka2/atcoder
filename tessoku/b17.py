# -*- coding: utf-8 -*-
N = int(input())
H = list(map(int, input().split()))
H.insert(0,0)

dp = [0] * (N+1)
dp[1] = 0
dp[2] = abs(H[1]-H[2])
for i in range(3,N+1):
    dp[i] = min(dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2]))

# ゴールからたどる
ans = [N]
currentPos = N
currentCost = dp[N]
while currentPos != 1:
    a = currentCost - abs(H[currentPos] - H[currentPos-1])
    if a == dp[currentPos-1]:
        currentCost  = dp[currentPos-1]
        currentPos -= 1
        ans.append(currentPos)
        continue
    b = currentCost - abs(H[currentPos] - H[currentPos-2])
    if b == dp[currentPos-2]:
        currentCost = dp[currentPos-2]
        currentPos -= 2
        ans.append(currentPos)

ans.reverse()
print(len(ans))
print(*ans)