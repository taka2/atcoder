# -*- coding: utf-8 -*-
N = int(input())

ans = 0
for i in range(1,1000001):
    if int(str(i)+str(i)) <= N:
        ans += 1

print(ans)