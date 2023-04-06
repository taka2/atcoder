# -*- coding: utf-8 -*-
N,K = map(int, input().split())
a = list(map(int, input().split()))

dp = [False] * (N+1)

for i in range(N+1):
    for j in range(K):
        if i >= a[j] and dp[i-a[j]] == False:
            dp[i] = True

if dp[N] == True:
    print("First")
else:
    print("Second")