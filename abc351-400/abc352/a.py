# -*- coding: utf-8 -*-
N,X,Y,Z = map(int, input().split())

ans = False
if X>Y:
    for i in range(Y,X+1):
        if i == Z:
            ans = True
else:
    for i in range(X,Y+1):
        if i == Z:
            ans = True

if ans:
    print("Yes")
else:
    print("No")