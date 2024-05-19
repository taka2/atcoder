# -*- coding: utf-8 -*-
N = int(input())
D,X = map(int, input().split())
A = []
for i in range(N):
    A.append(int(input()))

ans = X
for i in range(N):
    Ai = A[i]
    if D % Ai == 0:
        ans += D//Ai
    else:
        ans += (D//Ai) + 1

print(ans)