# -*- coding: utf-8 -*-
A = []
while True:
    Ai = input()
    A.append(Ai)
    if Ai == "0":
        break

for i in range(len(A)-1, -1, -1):
    print(A[i])