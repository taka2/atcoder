# -*- coding: utf-8 -*-
N = int(input())
APX = []
for i in range(N):
    A,P,X = map(int, input().split())
    APX.append((A,P,X))

ans = 10**9+1

for i in range(N):
    (A,P,X) = APX[i]
    zaiko = X-A
    if zaiko > 0:
        ans = min(ans, P)

if ans == 10**9+1:
    print("-1")
else:
    print(ans)