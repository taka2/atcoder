# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10000000)
from collections import defaultdict

T = int(input())
TestCases = []
ans = []
for i in range(T):
    N,M = map(int, input().split())
    C = [0] + list(map(int, input().split()))
    path = defaultdict(list)
    for i in range(M):
        v1,v2 = map(int, input().split())
        path[v1].append(v2)
        path[v2].append(v1)
    TestCases.append((N,M,C,path))

for i in range(T):
    (N,M,C,path) = TestCases[i]
    visitedT = [0] * (N+1)
    visitedA = [0] * (N+1)
    visitedX = [False]
    def dfs(posT, posA):
        visitedT[posT] = True
        visitedA[posA] = True
        if posT == N and posA == 1:
            visitedX[0] = True
            return
        for i in range(len(path[posT])):
            for j in range(len(path[posA])):
                nexT = path[posT][i]
                nexA = path[posA][j]
                if visitedT[nexT] or visitedA[nexA] or C[nexT] == C[nexA]:
                    pass
                else:
                    dfs(nexT, nexA)
                
    dfs(1, N)
    if visitedX[0]:
        ans.append("Yes")
    else:
        ans.append("-1")

print("--")
print(ans)