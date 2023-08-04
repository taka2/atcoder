# -*- coding: utf-8 -*-
import itertools

N,K = map(int, input().split())
T = []
for i in range(N):
    row = list(map(int, input().split()))
    T.append(row)

ans = 0
for elem in itertools.permutations(list(range(2,N+1)), N-1):
    cost = 0
    # 1から
    cost += T[0][elem[0]-1]
    # 途中
    for i in range(len(elem)-1):
        cost += T[elem[i]-1][elem[i+1]-1]
    # 1へ
    cost += T[elem[len(elem)-1]-1][0]

    if cost == K:
        ans += 1

print(ans)