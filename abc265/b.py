# -*- coding: utf-8 -*-
n,m,t = map(int, input().split())
a = list(map(int, input().split()))
bonusMap = {}

for i in range(m):
    x,y = map(int, input().split())
    bonusMap[x] = y

currentT = t
result = True
for i in range(1,n):
    # コストがかかる
    currentT -= a[i-1]
    
    # Tが0以下なら終了
    if currentT <= 0:
        result = False
        break

    # ボーナスもらう
    if (i+1) in bonusMap:
        currentT += bonusMap[i+1]

if result:
    print("Yes")
else:
    print("No")

