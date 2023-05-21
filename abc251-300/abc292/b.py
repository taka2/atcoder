# -*- coding: utf-8 -*-
from collections import defaultdict

N,Q = map(int, input().split())
mapa = defaultdict(int)
for i in range(Q):
    a,b = map(int, input().split())
    if a == 1:
        mapa[b] += 1
    elif a == 2:
        mapa[b] += 2
    else:
        if mapa[b] >= 2:
            print("Yes")
        else:
            print("No")