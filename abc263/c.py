# -*- coding: utf-8 -*-
import itertools

n,m = map(int, input().split())

for combi in itertools.combinations(range(1,m+1), n):
    print(" ".join(list(map(str, combi))))