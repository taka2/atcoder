# -*- coding: utf-8 -*-
N,T,P = map(int, input().split())
L = list(map(int, input().split()))

sortedL = sorted(L, reverse=True)

ans = 0
sum = 0
for i in range(N):
    if sortedL[i] >= T:
        pass
    else:
        ans = T-sortedL[i]

    sum += 1
    if sum >= P:
        break

print(ans)