# -*- coding: utf-8 -*-
N,A,B = map(int, input().split())
S = input()

ans = 10**9 * 5000 * 5000
for i in range(N):
    Ayen = A * i
    count = 0
    for j in range(N//2):
        if S[(j+i+N)%N] != S[(N-1+i-j)%N]:
            count += 1
    Byen = B * count
    ans = min(ans, Ayen+Byen)

print(ans)