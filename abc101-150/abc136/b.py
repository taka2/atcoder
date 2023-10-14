# -*- coding: utf-8 -*-
N = int(input())

ans = 0
for i in range(1,N+1):
    strNumber = str(i)
    if len(strNumber) % 2 == 1:
        ans += 1

print(ans)