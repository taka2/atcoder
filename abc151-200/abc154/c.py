# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

mapA = {}
ans = True
for i in range(N):
    Ai = A[i]
    if Ai in mapA:
        ans = False
        break
    else:
        mapA[Ai] = 1

if ans:
    print("YES")
else:
    print("NO")