# -*- coding: utf-8 -*-
import heapq
from collections import defaultdict

N,M = map(int, input().split())
G = defaultdict(list)
for i in range(M):
    A,B,C = map(int, input().split())
    G[A].append((B,C))
    G[B].append((A,C))

kakutei = [False] * (N+1)
cur = [10 ** 20] * (N+1)
Q = []

# スタート地点をキューに追加
cur[1] = 0
heapq.heappush(Q, (cur[1], 1))

# ダイクストラ法
while (len(Q) > 0):
    # 次に確定させるべき頂点を求める
    pos = heapq.heappop(Q)[1]

    # Qの最小要素が「既に確定した頂点」の場合
    if kakutei[pos]:
        pass

    # cur[x]の値を更新する
    kakutei[pos] = True
    for i in G[pos]:
        nex = i[0]
        cost = i[1]
        if(cur[nex] > cur[pos] + cost):
            cur[nex] = cur[pos] + cost
            heapq.heappush(Q, (cur[nex], nex))

for i in range(1, N+1):
    if cur[i] == 10 ** 20:
        print("-1")
    else:
        print(cur[i])