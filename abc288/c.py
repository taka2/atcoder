# -*- coding: utf-8 -*-
from collections import defaultdict

N,M = map(int, input().split())
hen = defaultdict(list)
for i in range(M):
    A,B = map(int, input().split())
    hen[A].append(B)
    hen[B].append(A)

globalVisited = []

def dfs(pos, visited):
    for i in range(len(hen[pos])):
        nex = hen[pos][i]
        if len(visited) >= 3 and nex == visited[0]:
            return visited
        if nex not in visited and nex not in globalVisited:
            visited.append(nex)
            return dfs(nex, visited)

    return visited

ans = 0

for i in range(1,N+1):
    if i not in globalVisited:
        dfsResult = dfs(i, [i])
        if len(dfsResult) >= 3:
            ans += 1
        globalVisited.extend(dfsResult)

print(ans)