# -*- coding: utf-8 -*-
import itertools

N = input()
listN = list(N)

ans = 0
for elem in itertools.permutations(listN, len(N)):
    for i in range(1,len(N)):
        l = ""
        r = ""
        for j in range(i):
            l += elem[j]
        for j in range(i,len(N)):
            r += elem[j]
        if l[0] == '0' or r[0] == '0':
            continue
        ans = max(ans, int(l)*int(r))

print(ans)