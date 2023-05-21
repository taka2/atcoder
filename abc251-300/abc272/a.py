# -*- coding: utf-8 -*-
# 整数の入力
n = int(input())
# スペース区切りの整数の入力
a = list(map(int, input().split()))

sum = 0
for i in range(len(a)):
    sum += a[i]

print(sum)