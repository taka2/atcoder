# -*- coding: utf-8 -*-
from collections import defaultdict

N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

events = []
for i in range(N):
    events.append((A[i], 0))
for j in range(M):
    events.append((B[j]+1, 1))

sortedEvents = sorted(events)

na = 0
nb = M
for event in sortedEvents:
    p = event[0]
    t = event[1]
    if t == 0:
        na += 1
    else:
        nb -= 1
    
    if (na >= nb):
        print(p)
        exit(0)