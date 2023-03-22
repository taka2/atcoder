# -*- coding: utf-8 -*-
H,W = map(int, input().split())
A = []
for i in range(H):
    B = ""
    Ai = list(map(int, input().split()))
    for j in range(W):
        if Ai[j] == 0:
            B += "."
        else:
            B += chr(65+Ai[j]-1)
    print(B)
