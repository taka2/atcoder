# -*- coding: utf-8 -*-
D,N = map(int, input().split())

base = 100**D
baseSQ = 100**(D+1)

if (base * N) % baseSQ == 0:
    print(base * (N+1))
else:
    print(base * N)