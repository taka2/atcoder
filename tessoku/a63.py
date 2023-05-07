# -*- coding: utf-8 -*-
from collections import deque, defaultdict

N,M = map(int, input().split())
G = defaultdict(list)

for i in range(M):
    A,B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

dist = [-1] * 100009

Q = deque()
Q.append(1)
dist[1] = 0

while(len(Q) > 0):
    pos = Q.popleft()
    for i in G[pos]:
        if dist[i] == -1:
            dist[i] = dist[pos] + 1
            Q.append(i)

for i in range(1,N+1):
    print(dist[i])