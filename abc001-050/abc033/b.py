# -*- coding: utf-8 -*-
N = int(input())
SP = []
sum = 0
for i in range(N):
    S,P = input().split()
    P = int(P)
    sum += P
    SP.append((S,P))

kahansu = sum // 2 + 1

ans = "atcoder"
for i in range(N):
    if SP[i][1] >= kahansu:
        ans = SP[i][0]
        break

print(ans)