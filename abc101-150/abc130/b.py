# -*- coding: utf-8 -*-
N,X = map(int, input().split())
L = list(map(int, input().split()))

ans = 1
currentPos = 0
for i in range(N):
    currentPos += L[i]
    if currentPos <= X:
        ans += 1

print(ans)