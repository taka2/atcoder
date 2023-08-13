# -*- coding: utf-8 -*-
X,Y = map(int, input().split())

ans = False
for i in range(X+1):
    sumLegs = i*2 + (X-i)*4
    if sumLegs == Y:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")