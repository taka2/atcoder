# -*- coding: utf-8 -*-
X,Y,Z = map(int, input().split())

n = X // (Y+Z)
if X - n*(Y+Z) < Z:
    n -= 1

print(n)