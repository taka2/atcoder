# -*- coding: utf-8 -*-
A,B = map(int, input().split())

ans = -1
for i in range(1,10001):
    if i*8//100 == A and i*10//100 == B:
        ans = i
        break

print(ans)