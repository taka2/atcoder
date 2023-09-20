# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

mapA = {}
for i in range(N):
    mapA[A[i]] = i+1

ans = []
for i in range(1,N+1):
    ans.append(mapA[i])

print(*ans)