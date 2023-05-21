# -*- coding: utf-8 -*-
N = int(input())

Smap = {1:["1"]}
for i in range(2,N+1):
    Si = Smap[i-1] + [str(i)] + Smap[i-1]
    Smap[i] = Si

print(*Smap[N])