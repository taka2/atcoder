# -*- coding: utf-8 -*-
N = input()
intN = int(N)

if intN % 3 == 0 or N.find("3") != -1:
    print("YES")
else:
    print("NO")