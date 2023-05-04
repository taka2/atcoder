# -*- coding: utf-8 -*-
from collections import defaultdict

N,M = map(int, input().split())
AB = []
for i in range(M):
    A,B = map(int, input().split())
    AB.append((A,B))

graph1 = defaultdict(list)
for i in range(M):
    (A,B) = AB[i]
    graph1[A].append(B)
    graph1[B].append(A)

for i in range(1,N+1):
    print(str(i) + ": {" + ", ".join(list(map(str, graph1[i]))) + "}")