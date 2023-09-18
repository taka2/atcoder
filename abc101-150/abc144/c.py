# -*- coding: utf-8 -*-
import math

N = int(input())

divisor = 1
for i in range(int(math.sqrt(N))+1,0,-1):
    if N % i == 0:
        divisor = i
        break

sho = N // divisor
ans = (divisor-1) + (sho-1)
print(ans)