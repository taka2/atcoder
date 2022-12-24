# -*- coding: utf-8 -*-
H,W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

def checkRowIsolated(row):
    isolated = []
    if row >= 0 and row < H:
        for j in range(W):
            current = A[row][j]
            up = 1-current
            if row != 0:
                up = A[row-1][j]
            down = 1-current
            if row != (H-1):
                down = A[row+1][j]
            left = 1-current
            if j != 0:
                left = A[row][j-1]
            right = 1-current
            if j != (W-1):
                right = A[row][j+1]
            if current != up and current != down and current != left and current != right:
                isolated.append((i,j))
    return isolated

def invertRow(row):
    if row >= 0 and row < H:
        for j in range(W):
            A[row][j] = 1 - A[row][j]

# 孤立マスを検出
isolated = []
for i in range(H):
    isolated.extend(checkRowIsolated(i))

clearRow = {}
flag = True
operationCount = 0
# 孤立マスを順番に処理
for isolatedCell in isolated:
    targetRow = isolatedCell[0]
    #print("isolatedCell",isolatedCell)
    # 反転前チェック
    if targetRow in clearRow:
        continue

    # 前の行
    if targetRow-1 >= 0 and targetRow-1 not in clearRow:
        invertRow(targetRow-1)
        checkBefore = checkRowIsolated(targetRow-2)
        checkCurrent = checkRowIsolated(targetRow-1)
        checkAfter = checkRowIsolated(targetRow)
        #print(targetRow-1,"before",checkBefore,checkCurrent,checkAfter)
        if len(checkBefore) == 0 and len(checkCurrent) == 0 and len(checkAfter) == 0:
            clearRow[targetRow - 2] = 1
            clearRow[targetRow - 1] = 1
            clearRow[targetRow - 0] = 1
            operationCount += 1
            continue
        else:
            # 戻す
            invertRow(targetRow-1)
    # カレント行
    if targetRow not in clearRow:
        invertRow(targetRow)
        checkBefore = checkRowIsolated(targetRow-1)
        checkCurrent = checkRowIsolated(targetRow)
        checkAfter = checkRowIsolated(targetRow+1)
        #print(targetRow,"current",checkBefore,checkCurrent,checkAfter)
        if len(checkBefore) == 0 and len(checkCurrent) == 0 and len(checkAfter) == 0:
            clearRow[targetRow - 1] = 1
            clearRow[targetRow] = 1
            clearRow[targetRow + 1] = 1
            operationCount += 1
            continue
        else:
            # 戻す
            invertRow(targetRow)
    # 後ろの行
    if targetRow+1 <= H-1 and targetRow+1 not in clearRow:
        invertRow(targetRow+1)
        checkBefore = checkRowIsolated(targetRow)
        checkCurrent = checkRowIsolated(targetRow+1)
        checkAfter = checkRowIsolated(targetRow+2)
        #print(targetRow+1,"after",checkBefore,checkCurrent,checkAfter)
        if len(checkBefore) == 0 and len(checkCurrent) == 0 and len(checkAfter) == 0:
            clearRow[targetRow] = 1
            clearRow[targetRow + 1] = 1
            clearRow[targetRow + 2] = 1
            operationCount += 1
            continue
        else:
            # 戻す
            invertRow(targetRow-1)
    # 孤立マス処理できなかった
    flag = False
    break

if(flag):
    print(operationCount)
else:
    print("-1")