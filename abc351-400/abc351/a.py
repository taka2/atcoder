# -*- coding: utf-8 -*-
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sumA = 0
sumB = 0
for i in range(9):
    sumA += A[i]

for i in range(8):
    sumB += B[i]

print(sumA-sumB+1)