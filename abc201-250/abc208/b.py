# -*- coding: utf-8 -*-
import math

P = int(input())
kouka = [0] * 11
for i in range(1, 11):
    kouka[i] = math.factorial(i)

ans = 0
for i in range(10, 0, -1):
    maisuu = P // kouka[i]
    ans += maisuu
    P -= (kouka[i] * maisuu)

print(ans)