# -*- coding: utf-8 -*-
import itertools

N,K = map(int, input().split())
A = list(map(int, input().split()))

# リストを二つに分ける
mid = N // 2 + 1
A1 = A[0:mid]
A2 = A[mid:]

sumA1 = {}
for i in range(len(A1)):
    for a1 in itertools.combinations(A1, i+1):
        sumA1[sum(a1)] = 1

sumA2 = {}
for i in range(len(A2)):
    for a2 in itertools.combinations(A2, i+1):
        sumA2[sum(a2)] = 1

ans = False
for i in sumA1:
    if i == K or (K-i) in sumA2:
        ans = True
        break

if(ans):
    print("Yes")
else:
    print("No")