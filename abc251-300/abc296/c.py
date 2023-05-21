# -*- coding: utf-8 -*-
N,X = map(int, input().split())
A = list(map(int, input().split()))

mapA = {}
for i in range(N):
    mapA[A[i]] = 1

ans = False
for An in mapA:
    if An+X in mapA or An-X in mapA:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")