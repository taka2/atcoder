# -*- coding: utf-8 -*-
Q = int(input())

map = {}
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        x = query[1]
        y = int(query[2])
        map[x] = y
    else:
        x = query[1]
        print(map[x])