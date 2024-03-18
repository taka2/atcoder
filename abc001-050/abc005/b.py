# -*- coding: utf-8 -*-
N = int(input())
ans = 101
for i in range(N):
    Ti = int(input())
    ans = min(ans, Ti)

print(ans)