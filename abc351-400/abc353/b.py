# -*- coding: utf-8 -*-
N,K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
zan = K
for i in range(N):
    if A[i] > zan:
        ans += 1
        zan = K-A[i]
    else:
        zan -= A[i]
ans += 1

print(ans)