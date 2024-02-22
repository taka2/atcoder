# -*- coding: utf-8 -*-
A = int(input())

ans = 0
for i in range(1,100):
    x = i
    y = A-x
    if y <= 0:
        continue

    a = x*y
    ans = max(ans, a)

print(ans)