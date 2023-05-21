# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10000000)

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

mapB = {}
for i in range(M):
    mapB[B[i]] = 1

visited = [0] * (X+1)
def dfs(pos):
    visited[pos] = True
    for i in range(N):
        nex = pos + A[i]
        if nex > X:
            pass
        elif visited[nex]:
            pass
        elif nex in mapB:
            pass
        else:
            dfs(nex)

dfs(0)
if visited[X]:
    print("Yes")
else:
    print("No")
