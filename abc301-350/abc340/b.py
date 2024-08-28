# -*- coding: utf-8 -*-
Q = int(input())
row = []
for i in range(Q):
    q1,q2 = map(int, input().split())
    if q1 == 1:
        row.append(q2)
    else:
        print(row[q2*-1])