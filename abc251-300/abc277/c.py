# -*- coding: utf-8 -*-
import sys
positions = {1:1}
ladders = {}
sys.setrecursionlimit(10000000)

def addPositions(n):
    # ポジションnからの昇り降りのはしごがある場合
    if n in ladders:
        # 移動先座標一覧
        toPositions = ladders[n]
        for i in range(len(toPositions)):
            # 移動先がポジション一覧に含まれていない場合は移動
            if toPositions[i] not in positions:
                positions[toPositions[i]] = 1
                addPositions(toPositions[i])

n = int(input())
for i in range(n):
    ladder = list(map(int, input().split()))
    if ladder[0] not in ladders:
        ladders[ladder[0]] = [ladder[1]]
    else:
        ladders[ladder[0]].append(ladder[1])

    if ladder[1] not in ladders:
        ladders[ladder[1]] = [ladder[0]]
    else:
        ladders[ladder[1]].append(ladder[0])

addPositions(1)
print(max(list(positions.keys())))