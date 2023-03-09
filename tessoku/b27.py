# -*- coding: utf-8 -*-
from decimal import *

A,B = map(int, input().split())
orgA = A
orgB = B

if A < B:
    tmp = B
    B = A
    A = tmp

ans = 0
while True:
    modb = B % A
    if modb == 0:
        ans = A
        break
    B = modb

    moda = A % B
    if moda == 0:
        ans = B
        break
    A = moda

print(Decimal(orgA)*Decimal(orgB)/Decimal(ans))