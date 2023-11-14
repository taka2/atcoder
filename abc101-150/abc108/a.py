# -*- coding: utf-8 -*-
K = int(input())

ans = 0
for i in range(1,K+1):
    for j in range(i+1,K+1):
        if i % 2 == 0 and j % 2 != 0:
            ans += 1
        elif i % 2 != 0 and j % 2 == 0:
            ans += 1

print(ans)