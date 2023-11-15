# -*- coding: utf-8 -*-
s = int(input())

map = {s:1}
i = 2
prev = s
while True:
    if prev % 2 == 0:
        n = prev // 2
        prev = n
    else:
        n = 3*prev+1
        prev = n
    if n in map:
        print(i)
        break
    map[n] = 1
    i += 1
