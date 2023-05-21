# -*- coding: utf-8 -*-
N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max = 0
for i in range(N):
    if A[i] > max:
        max = A[i]

maxIndex = {}
for i in range(N):
    if A[i] == max:
        maxIndex[i] = 1

result = False
for k in range(K):
    if (B[k]-1) in maxIndex:
        result = True
        break

if(result):
    print("Yes")
else:
    print("No")