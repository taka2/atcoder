# -*- coding: utf-8 -*-
N,D = map(int, input().split())
T = list(map(int, input().split()))

prev = 0
ans = -1
for i in range(N):
    if prev != 0:
        if (T[i] - prev) <= D:
            ans = T[i]
            break
    prev = T[i]

print(ans)