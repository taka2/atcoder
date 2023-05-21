# -*- coding: utf-8 -*-
import itertools

n,m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

result = 0
for c in itertools.combinations(s, 2):
    flag = True
    for i in range(m):
        if c[0][i] == 'x' and c[1][i] == 'x':
            flag = False
            break
    
    if flag:
        result += 1

print(result)