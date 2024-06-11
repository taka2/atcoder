# -*- coding: utf-8 -*-
from collections import defaultdict, deque

N1,N2,M = map(int, input().split())

path = defaultdict(list)
for i in range(M):
    a,b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)

# 幅優先探索の初期化（dist[i] = ? ではなく dist[i] = -1 で初期化していることに注意）
dist = [-1] * (N1+N2+1)
dist[1] = 0
dist[N1+N2] = 0
Q = deque()
Q.append(1)

# 幅優先探索
while len(Q) >= 1:
	pos = Q.popleft() # キュー Q の先頭要素を取り除き、その値を pos に代入する
	for nex in path[pos]:
		if dist[nex] == -1:
			dist[nex] = dist[pos] + 1
			Q.append(nex)

Q = deque()
Q.append(N1+N2)

# 幅優先探索
while len(Q) >= 1:
	pos = Q.popleft() # キュー Q の先頭要素を取り除き、その値を pos に代入する
	for nex in path[pos]:
		if dist[nex] == -1:
			dist[nex] = dist[pos] + 1
			Q.append(nex)

# 頂点 1 から各頂点までの最短距離を出力
#for i in range(1, N1+N2+1):
#	print(dist[i])

N1max = 0
for i in range(1, N1+1):
	N1max = max(N1max, dist[i])

N2max = 0
for i in range(N1+1, N1+N2+1):
	N2max = max(N2max, dist[i])

print(N1max+N2max+1)