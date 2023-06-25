# -*- coding: utf-8 -*-
x,y = map(int, input().split())

if x == y:
    print(x)
else:
    arr = [False] * 3
    arr[x] = True
    arr[y] = True
    for i in range(3):
        if not arr[i]:
            print(i)