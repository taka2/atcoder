# -*- coding: utf-8 -*-
N = int(input())
H = list(map(int, input().split()))

current = 0
ans = 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        current += 1
    else:
        ans = max(ans, current)
        current = 0

ans = max(ans, current)
print(ans)