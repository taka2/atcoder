# -*- coding: utf-8 -*-
N = int(input())
An = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        k = operation[1]-1
        x = operation[2]
        An[k] = x
    else:
        k = operation[1]-1
        print(An[k])
