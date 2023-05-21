# -*- coding: utf-8 -*-
import math

T = int(input())
for t in range(T):
    N = int(input())
    for i in range(2,2080084):
        if N % i != 0:
            continue
        if N % (i*i) == 0:
            p = i
            q = N // (p*p)
            print(p,q)
            break
        else:
            q = i
            p = int(math.sqrt(N/q))
            print(p,q)
            break

