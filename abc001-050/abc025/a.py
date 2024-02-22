# -*- coding: utf-8 -*-
S = input()
N = int(input())

index = 1
for i in range(len(S)):
    for j in range(len(S)):
        if index == N:
            print(S[i]+S[j])
            exit(0)
        index += 1