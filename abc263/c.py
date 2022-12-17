# -*- coding: utf-8 -*-
import itertools

n,m = map(int, input().split())

baselist = []
for i in range(m):
    baselist.append(i+1)

for combi in itertools.combinations(baselist, n):
    print(" ".join(list(map(str, combi))))