# -*- coding: utf-8 -*-
import math

N = int(input())
prime = [True] * (N+1)

for i in range(2, int(math.sqrt(N))+1):
    if prime[i] == False:
        continue
    for j in range(i*2, N+1, i):
        prime[j] = False

for i in range(2, N+1):
    if prime[i]:
        print(i)