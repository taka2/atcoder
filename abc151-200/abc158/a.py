# -*- coding: utf-8 -*-
S = input()

countA = 0
countB = 0
for i in range(len(S)):
    if S[i] == 'A':
        countA += 1
    else:
        countB += 1

if countA == 0 or countB == 0:
    print("No")
else:
    print("Yes")