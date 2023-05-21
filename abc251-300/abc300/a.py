# -*- coding: utf-8 -*-
N,A,B = map(int, input().split())
C = list(map(int, input().split()))

SUM = A+B
for i in range(N):
    if C[i] == SUM:
        print(i+1)