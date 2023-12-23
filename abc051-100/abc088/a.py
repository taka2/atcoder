# -*- coding: utf-8 -*-
N = int(input())
A = int(input())

Ndash = N%500
if A>=Ndash:
    print("Yes")
else:
    print("No")