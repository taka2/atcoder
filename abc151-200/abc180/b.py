# -*- coding: utf-8 -*-
import math

N = int(input())
x = list(map(int, input().split()))

dism = 0
for i in range(N):
    dism += abs(x[i])

disu = 0
for i in range(N):
    disu += x[i] ** 2
disu = math.sqrt(disu)

absx = []
for i in range(N):
    absx.append(abs(x[i]))

disc = max(absx)

print(dism)
print(disu)
print(disc)