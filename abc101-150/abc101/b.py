# -*- coding: utf-8 -*-
N = input()
intN = int(N)
sumN = 0
for i in range(len(N)):
    sumN += int(N[i])

if intN % sumN == 0:
    print("Yes")
else:
    print("No")