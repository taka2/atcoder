# -*- coding: utf-8 -*-
import math
a,b = input().split()

ab = int(a+b)
sqrtab = math.sqrt(ab)
if sqrtab == int(sqrtab):
    print("Yes")
else:
    print("No")