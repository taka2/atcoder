# -*- coding: utf-8 -*-
X,Y = map(int, input().split())

if X-Y <= 3 and X-Y > 0:
    print("Yes")
elif Y-X <= 2 and Y-X > 0:
    print("Yes")
else:
    print("No")