# -*- coding: utf-8 -*-
from collections import defaultdict
N = int(input())

nodeMap = defaultdict(int)
for i in range(N-1):
    a,b = map(int, input().split())
    nodeMap[a] += 1
    nodeMap[b] += 1

flag = False
for i in range(1,N+1):
    if nodeMap[i] == 1:
        pass
    if nodeMap[i] == (N-1):
        if not flag:
            flag = True
        else:
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")