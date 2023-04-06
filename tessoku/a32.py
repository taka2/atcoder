# -*- coding: utf-8 -*-
N,A,B = map(int, input().split())

dp = [False] * (N+1)

for i in range(N+1):
    if i >= A and dp[i-A] == False:
        dp[i] = True
    elif i >= B and dp[i-B] == False:
        dp[i] = True

if dp[N] == True:
    print("First")
else:
    print("Second")