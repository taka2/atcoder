# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10000000)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

H,W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())

visited = [[False] * (W) for i in range(H)]
mapCh = {'s':'n', 'n':'u', 'u':'k', 'k':'e', 'e':'s'}

def getNextCh(ch):
    return mapCh[ch]

def dfs(posx, posy, currentch):
    visited[posy][posx] = True
    nextCh = getNextCh(currentch)

    for k in range(4):
        nx = posx + dx[k]
        ny = posy + dy[k]
        if (ny < 0 or ny >= H or nx < 0 or nx >= W):
            continue
        if S[ny][nx] != nextCh:
            continue
        if visited[ny][nx]:
            continue
        dfs(nx,ny,nextCh)

if S[0][0] != 's':
    print("No")
    exit(0)

dfs(0,0,'s')

if visited[H-1][W-1] == True:
    print("Yes")
else:
    print("No")