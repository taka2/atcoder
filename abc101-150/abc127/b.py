# -*- coding: utf-8 -*-
r,D,x2000 = map(int, input().split())

prev = x2000
for i in range(2001,2011):
    xiplus1 = r*prev - D
    prev = xiplus1
    print(xiplus1)