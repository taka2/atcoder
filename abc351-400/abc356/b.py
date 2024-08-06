# -*- coding: utf-8 -*-
N,M = map(int, input().split())
A = list(map(int, input().split()))
sumA = [0] * M

for i in range(N):
    X = list(map(int, input().split()))
    for j in range(M):
        sumA[j] += X[j]

ans = True
for i in range(M):
    if sumA[i] < A[i]:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")