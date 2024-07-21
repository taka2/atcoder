# -*- coding: utf-8 -*-
N = int(input())
H = list(map(int, input().split()))

ans = -1
for i in range(1,N):
    if H[i] > H[0]:
        ans = i+1
        break

print(ans)