# -*- coding: utf-8 -*-
import itertools

# 整数の入力
n = int(input())
p = tuple(map(int, input().split()))

baseList = list(range(n+1))
baseList.pop(0)

prev = ()
for i in itertools.permutations(baseList):
    if p == i:
        print(" ".join(map(str, prev)))
        break
    else:
        prev = i