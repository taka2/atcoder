# -*- coding: utf-8 -*-
N,M = map(int, input().split())
B = []

for i in range(N):
    listB = list(map(int, input().split()))
    B.append(listB)

ans = True
amariFirstRow = []
for i in range(N):
    if len(amariFirstRow) == 0:
        # 先頭行
        for j in range(M):
            amariFirstRow.append(B[i][j] % 7)

    amariPrevColumn = -1
    for j in range(M):
        amari = B[i][j] % 7
        if amari != amariFirstRow[j]:
            # 先頭行の余りと合致していない
            ans = False
            break
        if amariPrevColumn == -1:
            # 先頭桁
            amariPrevColumn = amari
        else:
            if amari - amariPrevColumn != 1:
                # 前の桁と連続してない
                ans = False
                break
            else:
                amariPrevColumn = amari
   
    if not ans:
        break

if ans:
    print("Yes")
else:
    print("No")