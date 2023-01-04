# -*- coding: utf-8 -*-
N = input()

sum = 0
for i in range(len(N)):
    kurai = len(N)-i-1
    sum += int(N[i]) * (2**kurai)

print(sum)