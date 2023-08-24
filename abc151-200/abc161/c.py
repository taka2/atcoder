# -*- coding: utf-8 -*-
N,K = map(int, input().split())
if N>=K:
    t = N%K
else:
    t = N

print(min(t, K-t))