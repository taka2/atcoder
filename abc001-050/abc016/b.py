# -*- coding: utf-8 -*-
A,B,C = map(int, input().split())

plus = A+B
minus = A-B

if C==plus and C==minus:
    print("?")
elif C==plus:
    print("+")
elif C==minus:
    print("-")
else:
    print("!")