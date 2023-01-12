# -*- coding: utf-8 -*-
# 二分探索
# A: 探索対象の配列（1オリジン）
# X: 探す値
# return: インデックス
def search(A, X):
    l = 1
    r = N

    while(l<=r):
        m = (l+r)//2
        if X < A[m]:
            r = m - 1
        if X == A[m]:
            return m - 1
        if X > A[m]:
            l = m + 1
    
    return max(l,r)-1

N = int(input())
A = list(map(int, input().split()))
sortedA = sorted(A)
sortedA.insert(0,0)
Q = int(input())
for i in range(Q):
    X = int(input())
    ans = search(sortedA, X)
    print(ans)