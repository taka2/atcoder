# -*- coding: utf-8 -*-
N,Q = map(int, input().split())
A = list(map(int, input().split()))

Asum = []
sum = 0
for i in range(N):
    sum += A[i]
    Asum.append(sum)

for i in range(Q):
    L,R = map(int, input().split())
    Lvalue = 0
    if L-2 >= 0:
        Lvalue = Asum[L-2]
    print(Asum[R-1] - Lvalue)