# -*- coding: utf-8 -*-
X,Y = map(int, input().split())

ans = (Y - X) // 10
ansm = (Y - X) % 10

if ans < 0:
    ans = 0
elif ansm != 0:
    ans += 1
print(ans)