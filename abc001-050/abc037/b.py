# -*- coding: utf-8 -*-
N,Q = map(int, input().split())
LRT = []
for i in range(Q):
    L,R,T = map(int, input().split())
    LRT.append((L,R,T))

ans = []
for i in range(N):
    ans.append(0)

for i in range(Q):
    (L,R,T) = LRT[i]
    for j in range(L-1, R):
        ans[j] = T

for i in range(N):
    print(ans[i])