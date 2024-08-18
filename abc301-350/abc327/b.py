# -*- coding: utf-8 -*-
B = int(input())

ans = -1
for i in range(1,16):
    if B == i**i:
        ans = i
        break

print(ans)