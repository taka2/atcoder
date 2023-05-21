# -*- coding: utf-8 -*-
N,M,X,T,D = map(int, input().split())

if X>=M:
    print(T-(X-M)*D)
else:
    print(T)