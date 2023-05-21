# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

B = [0] * (N+1)
for i in range(N):
    if B[i+1] == 0:
        B[A[i]] = 1

C = []
for i in range(1, N+1):
    if B[i] == 0:
        C.append(i)

print(len(C))
print(*C)