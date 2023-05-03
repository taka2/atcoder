# -*- coding: utf-8 -*-
H,W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(input()))
B = []
for i in range(H):
    B.append(list(input()))

def copy2darr(A):
    copyA = []
    for i in range(H):
        copyA.append(A[i].copy())
    return copyA

def shift(A,i,j):
    Adash = copy2darr(A)
    # 縦方向のシフト
    for tate in range(j):
        Adash = Adash[1:] + [Adash[0]]

    # 横方向のシフト
    for h in range(H):
        for yoko in range(i):
            AdashLine = Adash[h]
            AdashLine = AdashLine[1:] + [AdashLine[0]]
            Adash[h] = AdashLine
    return Adash

def judge(A,B):
    ret = True
    for i in range(H):
        for j in range(W):
            if A[i][j] != B[i][j]:
                ret = False
                break
        if not ret:
            break
    return ret

ans = False
for i in range(W):
    for j in range(H):
        Adash = shift(A,i,j)
        if judge(Adash, B):
            ans = True
            break
    if ans:
        break

if ans:
    print("Yes")
else:
    print("No")