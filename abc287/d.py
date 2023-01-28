# -*- coding: utf-8 -*-
S = input()
T = input()

def hantei(sindex, tindex):
    if S[sindex] == '?' or T[tindex] == '?' or [sindex] == T[tindex]:
        return True
    else:
        return False

lenT = len(T)
prevOk = -1
for i in range(lenT+1):
    ans = True
    if prevOk == -1:
        prevOk = 0
        # 初回ループ
        startIndex = i-lenT
        for j in range(lenT-i):
            if hantei(startIndex+j, j):
                prevOk += 1
            else:
                ans = False
    else:
        # 二周目以降
        Ok = prevOk
        # 新たに判定に加わる
        if hantei(i-1, i-1):
            Ok += 1
        else:
            Ok -= 1

        # 判定から外れる
        sindex = i-lenT-1
        if hantei(sindex, i-1):
            Ok -= 1
        else:
            Ok += 1

        if Ok != lenT:
            ans = False
        prevOk = Ok

    if(ans):
        print("Yes")
    else:
        print("No")