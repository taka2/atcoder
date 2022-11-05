# -*- coding: utf-8 -*-
# 整数の入力
n, m = map(int, input().split())

# 初期化
bridges = [""]
for i in range(n):
    bridges.append([])

# 橋の数だけループ
for i in range(m):
    a, b = map(int, input().split())
    bridges[a].append(b)
    bridges[b].append(a)

for i in range(n+1):
    if(i != 0):
        strList = map(str, sorted(bridges[i]))
        print(str(len(bridges[i])), " ".join(strList))
