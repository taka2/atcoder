# -*- coding: utf-8 -*-
N,M = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(M):
    ans += A[B[i]]

print(ans)