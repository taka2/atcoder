# -*- coding: utf-8 -*-
N = int(input())
s = []
for i in range(N):
    s.append(input())

for i in range(N):
    line = ""
    for j in range(N-1,-1,-1):
        line += s[j][i]
    print(line)