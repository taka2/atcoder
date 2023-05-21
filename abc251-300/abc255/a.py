# -*- coding: utf-8 -*-
r,c = map(int, input().split())
a = []
for i in range(2):
    a.append(input().split())

print(a[r-1][c-1])