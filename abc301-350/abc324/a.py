# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

A0 = A[0]
ans = True
for i in range(N):
    if A0 != A[i]:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")