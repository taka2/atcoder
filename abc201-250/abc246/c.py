# -*- coding: utf-8 -*-
N,K,X = map(int, input().split())
A = list(map(int, input().split()))

sortedA = sorted(A, reverse=True)

# 各商品になくなるまでクーポンを順番に適用
currentK = K
for i in range(N):
    availableK = sortedA[i] // X
    if availableK > currentK:
        sortedA[i] -= currentK * X
        currentK = 0
    else:
        sortedA[i] -= availableK * X
        currentK -= availableK
    
    if currentK == 0:
        break

# クーポンが余ったら残りに順番に適用
if currentK > 0:
    sortedA = sorted(sortedA, reverse=True)
    for i in range(N):
        sortedA[i] = 0
        currentK -= 1

        if currentK == 0:
            break

print(sum(sortedA))
