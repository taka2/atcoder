# -*- coding: utf-8 -*-
from functools import cmp_to_key

N = int(input())
SP = []
for i in range(N):
    (S,P) = input().split()
    SP.append((S,int(P),(i+1)))

def cmptuple(a,b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    else:
        if a[1] > b[1]:
            return -1
        elif a[1] < b[1]:
            return 1
        else:
            return 0

sortedSP = sorted(SP, key=cmp_to_key(cmptuple))

for i in range(N):
    print(sortedSP[i][2])