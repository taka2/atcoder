# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
D = int(input())
DList = []
for i in range(D):
    L,R = map(int, input().split())
    DList.append((L,R))

# 左累積max
ALmax = [0] * N
lmax = 0
for i in range(N):
    if A[i] > lmax:
        lmax = A[i]
    ALmax[i] = lmax

# 右累積max
ARmax = [0] * N
rmax = 0
for i in range(N-1, -1, -1):
    if A[i] > rmax:
        rmax = A[i]
    ARmax[i] = rmax

for i in range(D):
    (L,R) = DList[i]
    
    lmax = 0
    if(L > 1):
        lmax = ALmax[L-2]
    rmax = 0
    if(R < N):
        rmax = ARmax[R]
    print(max(lmax, rmax))
