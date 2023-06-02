# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
X = int(input())

sumA = 0
for i in range(N):
    sumA += A[i]

loopCount = X // sumA
nokori = X - (sumA * loopCount)

sum = 0
count = 0
for i in range(N):
    sum += A[i]
    count += 1
    if sum > nokori:
        break

print(loopCount * N + count)