# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

ans = 0
mapA = {}
for i in range(N*2):
    #print(i, A[i], mapA)
    if A[i] not in mapA:
        mapA[A[i]] = i
    else:
        leftPos = mapA[A[i]]
        if i - leftPos == 2:
            ans += 1

print(ans)