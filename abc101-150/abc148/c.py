# -*- coding: utf-8 -*-
import math

A,B = map(int, input().split())
gcdAB = math.gcd(A,B)

ans = gcdAB * A//gcdAB * B//gcdAB
print(ans)