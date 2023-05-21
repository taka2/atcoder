# -*- coding: utf-8 -*-
n = list(map(int, input().split()))
b = n[1]
sortedN = sorted(n)

if(sortedN[1] == b):
    print("Yes")
else:
    print("No")