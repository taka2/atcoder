# -*- coding: utf-8 -*-
N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

current = 1
currentA = 0
currentB = 0
ansA = []
ansB = []
while not(currentA == N and currentB == M):
    if currentA == N:
        ansB.append(current)
        current += 1
        currentB += 1 
    elif currentB == M:
        ansA.append(current)
        current += 1
        currentA += 1 
    elif A[currentA] < B[currentB]:
        ansA.append(current)
        current += 1
        currentA += 1
    else:
        ansB.append(current)
        current += 1
        currentB += 1

print(*ansA)
print(*ansB)