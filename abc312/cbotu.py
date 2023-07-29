# -*- coding: utf-8 -*-
from collections import defaultdict

N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sortedA = sorted(A)
sortedB = sorted(B, reverse=True)

i = 0
j = 0
kai = 0
uri = 0
price = 0

while True:
    if i == len(A):
        i = len(A)-1
    if j == len(B):
        j = len(B)-1

    Ai = sortedA[i]
    Bj = sortedB[j]
    if Ai <= Bj:
        # 需給が合致
        uri += 1
        i += 1
        kai += 1
        j += 1
        price = Ai
    else:
        # 需給不一致
        break

if price == 0:
    print(sortedB[0]+1)
else:
    print(price)