# -*- coding: utf-8 -*-
N,K,X = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(K):
    ans.append(A[i])

ans.append(X)

for i in range(K,N):
    ans.append(A[i])

print(*ans)