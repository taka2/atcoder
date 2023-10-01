# -*- coding: utf-8 -*-
A,B,C = map(int, input().split())

zan = A-B
if C >= zan:
    print(C-zan)
else:
    print(0)