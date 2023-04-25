# -*- coding: utf-8 -*-
N,Q = map(int, input().split())
A = [0] + list(range(1,N+1))

state = False
for i in range(Q):
    q = list(input().split())
    if q[0] == '1':
        x = int(q[1])
        y = int(q[2])
        if not state:
            A[x] = y
        else:
            A[N-x+1] = y
    elif q[0] == '2':
        state = not state
    else:
        x = int(q[1])
        if not state:
            print(A[x])
        else:
            print(A[N-x+1])