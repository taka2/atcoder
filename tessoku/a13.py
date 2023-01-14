# -*- coding: utf-8 -*-
N,K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        if A[j] - A[i] <= K:
            ans += 1
        else:
            break

print(ans)