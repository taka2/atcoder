# -*- coding: utf-8 -*-
n,x = map(int, input().split())

pos = (x-1)//n
str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(str[pos])