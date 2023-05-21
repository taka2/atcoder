# -*- coding: utf-8 -*-
from collections import defaultdict

N,M = map(int, input().split())
Vmap = defaultdict(list)
valueMap = defaultdict(int)
for i in range(M):
    v1,v2 = map(int, input().split())
    Vmap[v1].append(v2)
    Vmap[v2].append(v1)
    valueMap[v1] += 1
    valueMap[v2] += 1

# 始点・終点を探す
startPoint = -1
endPoint = -1
flag = True
for value in valueMap:
    if valueMap[value] == 1:
        if startPoint == -1:
            startPoint = value
        elif endPoint == -1:
            endPoint = value
        else:
            # ダメ：始点・終点が3つ以上はおかしい
            flag = False
            break

if startPoint == -1 or endPoint == -1 or not flag:
    print("No")
    exit(0)

# 始点から探索する
currentPoint = startPoint
tuukazumi = {}
tuukazumi[startPoint] = 1
ans = True
while currentPoint != endPoint:
    # 次のパスを取得
        nextPathList = Vmap[currentPoint]
        next = -1
        for j in range(len(nextPathList)):
            if nextPathList[j] in tuukazumi:
                pass
            else:
                if next != -1:
                    # ダメ：2つ以上の行先があるのはおかしい
                    ans = False
                    break
                else:
                    next = nextPathList[j]

        # ダメ：行先がないのもおかしい
        if next == -1:
            ans = False
            break

        tuukazumi[next] = 1
        currentPoint = next
        if(not ans):
            break

# 終点チェック
if(ans):
    nextPathList = Vmap[endPoint]
    for i in range(len(nextPathList)):
        if nextPathList[i] not in tuukazumi:
            ans = False
            break

# ダメ：通過したポイントと超点数が合わない場合
if len(tuukazumi) != N:
    ans = False

if(ans):
    print("Yes")
else:
    print("No")