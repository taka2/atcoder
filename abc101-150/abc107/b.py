# -*- coding: utf-8 -*-
H,W = map(int, input().split())
a = []
for i in range(H):
    row = list(input())
    a.append(row)

# 行の処理
aa = []
for i in range(H):
    flag = True
    for j in range(W):
        if a[i][j] == '#':
            flag = False
            break
    if not flag:
        aa.append(a[i])

# 列の処理
aaa = []
for i in range(len(aa)):
    aaa.append([])
for j in range(W):
    flag = True
    for i in range(len(aa)):
        if aa[i][j] == '#':
            flag = False
            break
    if not flag:
        for i in range(len(aa)):
            aaa[i].append(aa[i][j])

for i in range(len(aaa)):
    row = aaa[i]
    rowStr = ""
    for j in range(len(row)):
        rowStr += row[j]
    print(rowStr)