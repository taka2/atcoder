# -*- coding: utf-8 -*-
N,T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

Tmax = -1
Tindex = -1
for i in range(N):
    if C[i] == T and R[i] > Tmax:
        Tmax = R[i]
        Tindex = i

if Tindex != -1:
    print(Tindex+1)
    exit(0)

CF = C[0]
Fmax = R[0]
Findex = 0

for i in range(1,N):
    if C[i] == CF and R[i] > Fmax:
        Fmax = R[i]
        Findex = i

print(Findex+1)