# -*- coding: utf-8 -*-
N = input()
Ni = int(N)

sum = 0
for i in range(len(N)):
    sum += int(N[i])

if Ni % sum == 0:
    print("Yes")
else:
    print("No")