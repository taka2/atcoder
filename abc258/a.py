# -*- coding: utf-8 -*-
k = int(input())

h = k // 60 + 21
m = k % 60

print('{:d}:{:02d}'.format(h,m))