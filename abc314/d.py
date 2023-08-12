# -*- coding: utf-8 -*-
N = int(input())
S = input()
Q = int(input())
txc = []
for i in range(Q):
    t,x,c = input().split()
    txc.append((int(t),int(x),c))

listS = list(S)
flag = 0 # 0はプレーン、1は小文字化、2は大文字化
indexesAfterFlag = {}
toLowerMap = {}
toUpperMap = {}
for i in range(26):
    toLowerMap[chr(ord('A')+i)] = chr(ord('a')+i)
    toLowerMap[chr(ord('a')+i)] = chr(ord('a')+i)
    toUpperMap[chr(ord('a')+i)] = chr(ord('A')+i)
    toUpperMap[chr(ord('A')+i)] = chr(ord('A')+i)

for i in range(Q):
    (t,x,c) = txc[i]
    if t == 1:
        listS[x-1] = c
        if flag == 1 or flag == 2:
            indexesAfterFlag[x-1] = 1
    elif t == 2:
        flag = 1
        indexesAfterFlag = {}
    elif t == 3:
        flag = 2
        indexesAfterFlag = {}

if flag == 1 or flag == 2:
    for i in range(N):
        if i in indexesAfterFlag:
            pass
        else:
            if flag == 1:
                listS[i] = toLowerMap[listS[i]]
            elif flag == 2:
                listS[i] = toUpperMap[listS[i]]

ans = ""
for i in range(N):
    ans += listS[i]

print(ans)