# -*- coding: utf-8 -*-
N = int(input())
A = [0] + list(map(int, input().split()))

# 全部XORした値（ニム和）を求める
XOR_Sum = A[1]
for i in range(2, N+1):
    XOR_Sum  = XOR_Sum ^ A[i]

if XOR_Sum != 0:
    print("First")
else:
    print("Second")