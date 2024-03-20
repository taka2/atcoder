# -*- coding: utf-8 -*-
c = []
for i in range(4):
    c.append(input().split())

ans = []
for j in range(3, -1, -1):
    ansl = []
    for k in range(3, -1, -1):
        ansl.append(c[j][k])
    ans.append(ansl)

for i in range(4):
    print(*ans[i])