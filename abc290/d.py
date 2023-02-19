# -*- coding: utf-8 -*-
import math

T = int(input())
for i in range(T):
    N,D,K = map(int, input().split())
    if math.gcd(N,D) == 1:
        amari = ((K-1) * D) % N
        print(amari)
    else:
        DD = D
        if D > N:
            DD = D % N
            if DD == 0:
                DD = N
        shou = ((K-1) * DD) // N // (DD // math.gcd(N,DD))
        amari = ((K-1) * DD) % N
        print(shou+amari)