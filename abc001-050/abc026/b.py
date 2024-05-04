# -*- coding: utf-8 -*-
import math

N = int(input())
R = []
for i in range(N):
    R.append(int(input()))

sortedR = sorted(R, reverse=True)

ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += sortedR[i]**2
    else:
        ans -= sortedR[i]**2

ans *= math.pi
print(ans)