# -*- coding: utf-8 -*-
N = int(input())
SC = []
sumRate = 0
names = []
for i in range(N):
    S,C = input().split()
    C = int(C)
    sumRate += C
    names.append(S)
    SC.append((S,C))

sortedNames = sorted(names)
print(sortedNames[sumRate % N])