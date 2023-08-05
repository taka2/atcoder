# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

ans = 0
maxgcddegree = 0
for i in range(2,1001):
    gcddegree = 0
    for j in range(N):
        if A[j] % i == 0:
            gcddegree += 1
    if gcddegree > maxgcddegree:
        maxgcddegree = gcddegree
        ans = i

print(ans)