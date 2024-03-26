# -*- coding: utf-8 -*-
import math
N = int(input())
A = list(map(int, input().split()))

num = 0
sum = 0
for i in range(N):
    if A[i] != 0:
        num += 1
        sum += A[i]

print(math.ceil(sum/num))