# -*- coding: utf-8 -*-
import itertools

N,W = map(int, input().split())
A = list(map(int, input().split()))

resultMap = {}
# 1つ選ぶ場合
for i in range(N):
    if A[i] <= W:
        resultMap[A[i]] = 1

# 2つ選ぶ場合
for elem in itertools.combinations(A, 2):
    sum = elem[0] + elem[1]
    if sum <= W:
        resultMap[sum] = 1

# 3つ選ぶ場合
for elem in itertools.combinations(A, 3):
    sum = elem[0] + elem[1] + elem[2]
    if sum <= W:
        resultMap[sum] = 1

print(len(resultMap))