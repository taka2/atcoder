# -*- coding: utf-8 -*-
import math

N = int(input())

ans = math.floor(N * 1.08)
if ans < 206:
    print("Yay!")
elif ans > 206:
    print(":(")
else:
    print("so-so")