# -*- coding: utf-8 -*-
N,A,B = map(int, input().split())
sd = []
for i in range(N):
    s,d = input().split()
    d = int(d)
    sd.append((s,d))

current = 0
direction = 0

for i in range(N):
    (s,d) = sd[i]
    nd = d
    if nd < A:
        nd = A
    elif nd > B:
        nd = B
    
    #print("tochu",current, direction, s, nd)
    if s == "East":
        if direction == 0:
            direction = 1
            current += nd
        elif direction == 1:
            current += nd
        else:
            if current >= nd:
                current -= nd
            else:
                direction = 1
                current = nd - current
    else:
        if direction == 0:
            direction = -1
            current += nd
        elif direction == -1:
            current += nd
        else:
            if current >= nd:
                current -= nd
            else:
                direction = -1
                current = nd - current

#print("final", current, direction)
if current == 0:
    print(0)
elif direction == 1:
    print("East", current)
else:
    print("West", current)