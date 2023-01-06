# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

Asum = []
sum = 0
for i in range(N):
    sum += A[i]
    Asum.append(sum)

for i in range(Q):
    L,R = map(int, input().split())
    Lvalue = 0
    if L-2 >= 0:
        Lvalue = Asum[L-2]
    atari = Asum[R-1] - Lvalue
    kaisu = R-L+1
    hazure = kaisu - atari
    if atari > hazure:
        print("win")
    elif hazure > atari:
        print("lose")
    else:
        print("draw")