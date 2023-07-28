# -*- coding: utf-8 -*-
N = int(input())
sq = int(N**0.5)

s = set()
for a in range(2,sq+1):
    x = a**2
    while x <= N:
        s.add(x)
        x *= a

print(N-len(s))