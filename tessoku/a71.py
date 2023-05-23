# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sortedA = sorted(A)
sortedB = sorted(B, reverse=True)

ans = 0
for i in range(N):
    ans += (sortedA[i] * sortedB[i])

print(ans)