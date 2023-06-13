# -*- coding: utf-8 -*-
N,Q = map(int, input().split())
xq = []
for i in range(Q):
    xq.append(int(input()))

val = [-1]
for i in range(1,N+1):
    val.append(i)

pos = [-1]
for i in range(1,N+1):
    pos.append(i)

for i in range(Q):
    p0 = pos[xq[i]]
    p1 = p0
    if p0 != N:
        p1 += 1
    else:
        p1 -= 1

    v0 = val[p0]
    v1 = val[p1]

    tmpVal = val[p0]
    val[p0] = val[p1]
    val[p1] = tmpVal

    tmpPos = pos[v0]
    pos[v0] = pos[v1]
    pos[v1] = tmpPos

pos = pos[1:]
print(*pos)