# -*- coding: utf-8 -*-
N = int(input())
A = []
for i in range(N):
    A.append(input())
B = []
for i in range(N):
    B.append(input())

for i in range(N):
    for j in range(len(A[i])):
        if A[i][j] != B[i][j]:
            print(i+1, j+1)
            exit(0)