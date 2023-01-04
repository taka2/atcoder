# -*- coding: utf-8 -*-
N = int(input())
str = bin(N)[2:]

padding = ""
for i in range(10-len(str)):
    padding = padding + "0"

print(padding + str)