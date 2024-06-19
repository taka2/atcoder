# -*- coding: utf-8 -*-
N = input()

ans = True
prev = 10
for i in range(len(N)):
    Ni = int(N[i])
    if Ni < prev:
        prev = Ni
        continue
    else:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")