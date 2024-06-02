# -*- coding: utf-8 -*-
N = int(input())

for i in range(26):
    for j in range(15):
        sum = 4*i + 7*j
        if sum == N:
            print("Yes")
            exit(0)

print("No")