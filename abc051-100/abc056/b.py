# -*- coding: utf-8 -*-
W,a,b = map(int, input().split())

ans = abs(b-a)-W
if ans <= 0:
    print(0)
else:
    print(ans)

