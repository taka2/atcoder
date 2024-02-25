# -*- coding: utf-8 -*-
N,S,T = map(int, input().split())
W = int(input())
A = []
for i in range(N-1):
    A.append(int(input()))

ans = 0
current = W
if current >= S and current <= T:
    ans += 1
for i in range(N-1):
    current += A[i]
    if current >= S and current <= T:
        ans += 1
    
print(ans)