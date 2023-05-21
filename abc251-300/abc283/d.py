# -*- coding: utf-8 -*-
S = input()

# 箱：入ってるボールの文字をキーとするdict
box = {}
# 開きカッコの位置リスト
openKakkoList = []
# 開きカッコから閉じカッコまでに箱に入れた文字のリスト
charList = {}

result = True
for i in range(len(S)):
    if S[i] == '(':
        openKakkoList.append(i)
        charList[i] = []
    elif S[i] == ')':
        openKakkoIndex = openKakkoList.pop()
        targetChars = charList[openKakkoIndex]
        # カッコ内にいた文字を削除
        for ch in targetChars:
            del box[ch]
    else:
        if S[i] in box:
            result = False
            break
        else:
            box[S[i]] = 1
            if len(openKakkoList) > 0:
                charList[openKakkoList[-1]].append(S[i])

if(result):
    print("Yes")
else:
    print("No")