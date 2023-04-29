# -*- coding: utf-8 -*-
A,B,C = map(int, input().split())

ans = -1
for i in range(1,(1000//C+1)):
    D = i*C
    if D >= A and D <= B and D <= 1000:
        ans = D
        break

print(ans)