# -*- coding: utf-8 -*-
N = int(input())

a = N // 5
b = N - (a*5)
if b <= 2:
    print(a * 5)
else:
    print((a+1) * 5)