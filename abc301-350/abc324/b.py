# -*- coding: utf-8 -*-
N = int(input())

for i in range(100):
    for j in range(100):
        x = 2**i * 3**j
        if x == N:
            print("Yes")
            exit(0)
print("No")