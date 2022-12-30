# -*- coding: utf-8 -*-
N,Q = map(int, input().split())
S = input()

offset = 0
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        offset -= query[1]
    elif query[0] == 2:
        targetIndex = (query[1]+offset-1+N) % N
        print(S[targetIndex])
