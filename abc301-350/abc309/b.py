# -*- coding: utf-8 -*-
N = int(input())
A = []
for i in range(N):
    A.append(input())

B = []
for i in range(N):
    if i==0:
        B.append(str(A[i+1][0]) + str(A[i][0:N-1]))
    elif i==(N-1):
        B.append(str(A[i][1:]) + str(A[i-1][N-1]))
    else:
        B.append(str(A[i+1][0]) + str(A[i][1:N-1]) + str(A[i-1][N-1]))

for i in range(N):
    print(B[i])