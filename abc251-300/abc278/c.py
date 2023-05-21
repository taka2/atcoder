# -*- coding: utf-8 -*-
n, q = map(int, input().split())
follows = {}

for i in range(q):
    t,a,b = map(int, input().split())
    if t == 1:
        if a in follows:
            follows[a][b] = 1
        else:
            follows[a] = {b:1}
    elif t == 2:
        if a in follows and b in follows[a]:
            del follows[a][b]
    elif t == 3:
        if a in follows and b in follows[a] and b in follows and a in follows[b]:
            print("Yes")
        else:
            print("No")