# -*- coding: utf-8 -*-
H,W = map(int, input().split())
C = []
for i in range(H):
    Ci = list(input().split())
    C.append(Ci)

for i in range(H):
    Ci = C[i]
    print(*Ci)
    print(*Ci)