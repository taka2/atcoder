# -*- coding: utf-8 -*-
N = int(input())
h = N // 3600
zan = N - h * 3600
m = zan // 60
s = zan - m * 60

print('{:02}:{:02}:{:02}'.format(h,m,s))