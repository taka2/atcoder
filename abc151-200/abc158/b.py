# -*- coding: utf-8 -*-
N,A,B = map(int, input().split())

loops = N // (A+B)
amari = min(A, N % (A+B))

print(loops * A + amari)