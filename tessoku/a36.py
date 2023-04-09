# -*- coding: utf-8 -*-
N,K = map(int, input().split())
if K < (2*N-2) or K % 2 == 1:
    print("No")
else:
    print("Yes")