# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10000000)

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

    if posx == (W-1) and posy == (H-1):
        return

    nextCh = getNextCh(currentch)

    # Up
    if (posy - 1) > 0 and not visited[posy-1][posx] and S[posy-1][posx] == nextCh:
        dfs(posx, posy-1, nextCh)
    # Down
    if (posy + 1) < H and not visited[posy+1][posx] and S[posy+1][posx] == nextCh:
        dfs(posx, posy+1, nextCh)
    # Left
    if (posx - 1) > 0 and not visited[posy][posx-1] and S[posy][posx-1] == nextCh:
        dfs(posx-1, posy, nextCh)
    # Right
    if (posx + 1) < W and not visited[posy][posx+1] and S[posy][posx+1] == nextCh:
        dfs(posx+1, posy, nextCh)

if S[0][0] != 's':
    print("No")
    exit(0)

dfs(0,0,'s')

if visited[H-1][W-1] == True:
    print("Yes")
else:
    print("No")