# -*- coding: utf-8 -*-
A,B = map(int, input().split())

plus = A+B
minus = A-B
mult = A*B

print(max(max(plus, minus), mult))