# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
h, w = map(int, input().split())

# result配列の初期化
result = []
for j in range(w):
    result.append(0)

for i in range(h):
    row = list(input())
    for j in range(w):
        if (row[j] == '#'):
            result[j] = result[j] + 1

resultStr = map(str, result)
print(" ".join(resultStr))
