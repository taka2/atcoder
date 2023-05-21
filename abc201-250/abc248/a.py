# -*- coding: utf-8 -*-
S = input()
sortedS = sorted(S)

for i in range(len(S)):
    if int(sortedS[i]) != i:
        print(i)
        break
else:
    print(9)