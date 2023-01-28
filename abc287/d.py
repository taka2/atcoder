# -*- coding: utf-8 -*-
S = input()
T = input()

lenT = len(T)
for i in range(lenT+1):
    ans = True
    # 先頭i文字のチェック
    for j in range(i):
        if S[j] == '?' or T[j] == '?' or S[j] == T[j]:
            pass
        else:
            ans = False
            break
    # 残りの|T|-i文字のチェック
    if ans:
        startIndex = i-lenT
        for j in range(lenT-i):
            if S[startIndex+j] == '?' or T[j] == '?' or S[startIndex+j] == T[j]:
                pass
            else:
                ans = False
                break

    if(ans):
        print("Yes")
    else:
        print("No")