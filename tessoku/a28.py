# -*- coding: utf-8 -*-
N = int(input())
TA = []
for i in range(N):
    TA.append(input().split())

Answer = 0
for i in range(N):
    T,A = TA[i][0], int(TA[i][1])
    if T == '+':
        Answer += A
    elif T == '-':
        Answer -= A
    elif T == '*':
        Answer *= A
    
    if Answer < 0:
        Answer += 10000
    
    Answer %= 10000
    print(Answer)