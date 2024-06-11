# -*- coding: utf-8 -*-
N,M = map(int, input().split())
S = []
for i in range(N):
    S.append(input())

def judge(i,j):
    if S[i][j] != '#':
        return False
    if S[i+1][j] != '#':
        return False
    if S[i+2][j] != '#':
        return False
    if S[i][j+1] != '#':
        return False
    if S[i+1][j+1] != '#':
        return False
    if S[i+2][j+1] != '#':
        return False
    if S[i][j+2] != '#':
        return False
    if S[i+1][j+2] != '#':
        return False
    if S[i+2][j+2] != '#':
        return False

    if S[i+6][j+6] != '#':
        return False
    if S[i+7][j+6] != '#':
        return False
    if S[i+8][j+6] != '#':
        return False
    if S[i+6][j+7] != '#':
        return False
    if S[i+7][j+7] != '#':
        return False
    if S[i+8][j+7] != '#':
        return False
    if S[i+6][j+8] != '#':
        return False
    if S[i+7][j+8] != '#':
        return False
    if S[i+8][j+8] != '#':
        return False
    
    if S[i][j+3] != '.':
        return False
    if S[i+1][j+3] != '.':
        return False
    if S[i+2][j+3] != '.':
        return False
    if S[i+3][j] != '.':
        return False
    if S[i+3][j+1] != '.':
        return False
    if S[i+3][j+2] != '.':
        return False
    if S[i+3][j+3] != '.':
        return False

    if S[i+5][j+5] != '.':
        return False
    if S[i+5][j+6] != '.':
        return False
    if S[i+5][j+7] != '.':
        return False
    if S[i+5][j+8] != '.':
        return False
    if S[i+6][j+5] != '.':
        return False
    if S[i+7][j+5] != '.':
        return False
    if S[i+8][j+5] != '.':
        return False


    return True

ans = []
for i in range(N-9+1):
    for j in range(M-9+1):
        if judge(i,j):
            ans.append((i+1,j+1))

for i in range(len(ans)):
    print(ans[i][0], ans[i][1])