# -*- coding: utf-8 -*-
import math

a = int(input())
b = int(input())
n = int(input())

g = math.gcd(a,b)
x = g*a//g*b//g

ans = x
for i in range(20000):
    if ans >= n:
        print(ans)
        break
    ans += x