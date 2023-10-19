# -*- coding: utf-8 -*-
N,D = map(int, input().split())

scope = 1+D*2
if N % scope == 0:
    print(N//scope)
else:
    print(N//scope+1)