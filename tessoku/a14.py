# -*- coding: utf-8 -*-
N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

AB = {}
for i in range(N):
    for j in range(N):
        sum = A[i] + B[j]
        AB[sum] = 1

CD = {}
for i in range(N):
    for j in range(N):
        sum = C[i] + D[j]
        CD[sum] = 1

ans = False
for ab in AB:
    if (K-ab) in CD:
        ans = True
        break

if(ans):
    print("Yes")
else:
    print("No")