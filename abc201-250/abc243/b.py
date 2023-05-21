# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

hit = 0
blow = 0
for i in range(N):
    if B[i] == A[i]:
        hit += 1
    elif B[i] in A:
        blow += 1

print(hit)
print(blow)