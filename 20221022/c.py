# -*- coding: utf-8 -*-
# 整数の入力
a = int(input())
# スペース区切りの整数の入力
row = list(map(int, input().split()))

result = []
resultSize = 2*a+1+1

for i in range(resultSize):
    result.append(0)

for j in range(a):
    bunretsuAmeba = row[j]
    bunretsuSaki1 = (j+1)*2
    bunretsuSaki2 = (j+1)*2+1
    result[bunretsuSaki1] = result[bunretsuAmeba] + 1
    result[bunretsuSaki2] = result[bunretsuAmeba] + 1

# 先頭要素削除
result.pop(0)

# 結果表示
for k in range(len(result)):
    print(result[k])
