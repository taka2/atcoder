# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

for i in range(N+1):
    if i not in A:
        print(i)
        break
