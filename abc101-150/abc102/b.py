# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        diff = abs(A[i]-A[j])
        ans = max(ans, diff)

print(ans)