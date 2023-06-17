# -*- coding: utf-8 -*-
N = int(input())
XY = [(False,0)]
for i in range(N):
    X,Y = map(int, input().split())
    XY.append((X,Y))

# 無毒
dpTotala = [0] * (N+1)
# 有毒
dpTotalb = [0] * (N+1)

for i in range(1,N+1):
    (X,Y) = XY[i]
    if X == 0:
        # 解毒剤入りの場合
        dpTotala[i] = max(dpTotala[i-1]+Y, dpTotalb[i-1]+Y, dpTotala[i-1]) 
        dpTotalb[i] = dpTotalb[i-1]
    else:
        # 毒入りの場合
        dpTotala[i] = dpTotala[i-1]
        dpTotalb[i] = max(dpTotalb[i-1], dpTotala[i-1] + Y)

print(max(dpTotala[N], dpTotalb[N]))