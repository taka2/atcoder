# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

sum = 0
for i in range(N-1):
    sum += A[i]

print(sum * -1)