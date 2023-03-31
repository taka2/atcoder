# -*- coding: utf-8 -*-
A,B = map(int, input().split())

ans = False
while A > 0 and B > 0:
    modA = A%10
    modB = B%10
    if (modA + modB) >= 10:
        ans = True
        break
    A = A//10
    B = B//10

if ans:
    print("Hard")
else:
    print("Easy")