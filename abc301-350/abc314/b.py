# -*- coding: utf-8 -*-
N = int(input())
C = []
A = []
for i in range(N):
    C.append(int(input()))
    A.append(list(map(int, input().split())))
X = int(input())

minC = 100
ansList = []
for i in range(N):
    Ci = C[i]
    Ai = A[i]
    if X in Ai:
        if minC == Ci:
            ansList.append(i+1)
        elif Ci < minC:
            minC = Ci
            ansList = []
            ansList.append(i+1)

sortedAnsList = sorted(ansList)

print(len(sortedAnsList))
print(*sortedAnsList)