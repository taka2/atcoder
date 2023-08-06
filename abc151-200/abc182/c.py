# -*- coding: utf-8 -*-
import itertools

N = int(input())
Nketa = len(str(N))

def judge(arr):
    sum = 0
    for i in range(len(arr)):
        sum += int(arr[i])
    return sum % 3 == 0

ans = -1
for i in range(Nketa,0,-1):
    for elem in itertools.combinations(list(str(N)),i):
        if judge(elem):
            ans = Nketa - i
            break
    if ans != -1:
        break
    
print(ans)
