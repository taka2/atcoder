# -*- coding: utf-8 -*-
a = int(input())
b = int(input())

amari = a % b
if amari == 0:
    print(0)
else:
    print(b-amari)