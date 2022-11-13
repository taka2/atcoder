# -*- coding: utf-8 -*-
y = int(input())

amari = y % 4
if amari == 2:
    print(y)
elif amari == 0:
    print(y+2)
else:
    print(y+amari)