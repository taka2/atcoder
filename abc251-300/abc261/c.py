# -*- coding: utf-8 -*-
from collections import defaultdict

n = int(input())
countmap = defaultdict(int)

for i in range(n):
    s = input()
    if s in countmap:
        print(s + "(" + str(countmap[s]) + ")")
    else:
        print(s)
    countmap[s] += 1