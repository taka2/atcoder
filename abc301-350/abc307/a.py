# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

ans = []
weeksum = 0
for i in range(N*7):
    if i != 0 and i % 7 == 0:
        ans.append(weeksum)
        weeksum = 0
    weeksum += A[i]

ans.append(weeksum)

print(*ans)