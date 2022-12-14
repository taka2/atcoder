# -*- coding: utf-8 -*-
import itertools

n,m = map(int, input().split())
lines = {}
for i in range(m):
    u,v = map(str, input().split())
    lines[u+":"+v] = 1

baselist = []
for i in range(n):
    baselist.append(i+1)

result = []
for elem in itertools.combinations(baselist, 3):
    key1 = str(elem[0]) + ":" + str(elem[1])
    key2 = str(elem[1]) + ":" + str(elem[2])
    key3 = str(elem[0]) + ":" + str(elem[2])
    if key1 in lines and key2 in lines and key3 in lines:
        result.append(elem)

print(len(result))
