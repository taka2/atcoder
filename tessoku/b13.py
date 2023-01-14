# -*- coding: utf-8 -*-
N,K = map(int, input().split())
A = list(map(int, input().split()))
A.insert(0,0)
R = [0] * (N+1)

def sum(fr,to):
    sum = 0
    for i in range(fr, to):
        sum += A[i]
    return sum

# しゃくとり法
for i in range(1,N+1):
    # スタート地点を決める
    if i == 1:
        R[i] = 1
    else:
        R[i] = R[i-1]

    # ギリギリまで増やしていく
    while (R[i] <= N and sum(i, R[i]+1) <= K):
        R[i] += 1

# 出力
ans = 0
for i in range(1,N+1):
    ans += (R[i]-i)
print(ans)
