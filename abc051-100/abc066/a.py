# -*- coding: utf-8 -*-
a,b,c = map(int, input().split())

maxabc = max(max(a,b), c)
if a == maxabc:
    print(b+c)
elif b == maxabc:
    print(a+c)
else:
    print(a+b)