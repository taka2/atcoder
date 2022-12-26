# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10000000)

N,X,Y = map(int, input().split())
U = {}
for i in range(N-1):
    path = list(map(int, input().split()))
    if path[0] in U:
        U[path[0]].append(path[1])
    else:
        U[path[0]] = [path[1]]
    
    if path[1] in U:
        U[path[1]].append(path[0])
    else:
        U[path[1]] = [path[0]]

def search(currentpath):
    current = currentpath[-1]
    if current == Y:
        return currentpath
    nextpath = U[current]
    prev = -1
    if len(currentpath) >= 2:
        prev = currentpath[-2]
    for i in nextpath:
        if prev == -1 or i != prev:
            currentpath.append(i)
            resultPath = search(currentpath)
            if resultPath != None:
                return resultPath
            else:
                currentpath.pop()

current = [X]
result = search(current)
print(" ".join(list(map(str, result))))