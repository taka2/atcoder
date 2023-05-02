# -*- coding: utf-8 -*-
import bisect

Q = int(input())

map = {}
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        x = int(query[1])
        map[x] = 1
    elif query[1] == '2':
        x = int(query[1])
        del map[x]
    else:
        x = int(query[1])
        sortedMap = sorted(map.keys())
        pos = bisect.bisect_left(sortedMap, x)
        if pos == len(sortedMap):
            print("-1")
        else:
            print(sortedMap[pos])