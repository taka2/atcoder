# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10000000)

from collections import defaultdict

N,M = map(int, input().split())
G = defaultdict(list)

for i in range(M):
    A,B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

visited = [False] * 100009

def dfs(pos):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i)

dfs(1)

ans = "The graph is connected."
for i in range(N):
    if visited[i+1] == False:
        ans = "The graph is not connected."
        break

print(ans)