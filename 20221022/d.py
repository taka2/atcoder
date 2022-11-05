# -*- coding: utf-8 -*-
def hantei(goal, movelist):
    list = {0: 0}
    for elem in movelist:
        resultList = {}
        for a in list:
            plus = a + elem
            minus = a - elem
            if (plus not in resultList):
                resultList[plus] = 0
            if (minus not in resultList):
                resultList[minus] = 0
        list = resultList

    return goal in list


# スペース区切りの整数の入力
n, x, y = map(int, input().split())
# スペース区切りの整数の入力
row = list(map(int, input().split()))

currentX = row[0]

# 先頭要素削除
row.pop(0)

listX = []
listY = []
for i in range(len(row)):
    if (i % 2 == 0):
        listY.append(row[i])
    else:
        listX.append(row[i])

if (hantei(x-currentX, listX) and hantei(y, listY)):
    print("Yes")
else:
    print("No")
