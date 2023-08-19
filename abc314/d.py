# -*- coding: utf-8 -*-
N = int(input())
S = input()

status = []
for i in range(N):
    status.append((0, S[i]))

Q = int(input())

fill = None

for i in range(Q):
    t,x,c = input().split()
    t = int(t)
    x = int(x)

    if t == 1:
        status[x-1] = (i,c)
    else:
        fill = (i,t)

ans = ""
for i in range(N):
    (time,c) = status[i]
    if fill == None or time >= fill[0]:
        ans += c
    elif fill[1] == 2:
        ans += c.lower()
    else:
        ans += c.upper()

print(ans)