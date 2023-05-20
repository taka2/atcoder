# -*- coding: utf-8 -*-
H,W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())

def check(i,j):
    if j >= 4:
        # 左
        if S[i][j-1] == 'n' and S[i][j-2] == 'u' and S[i][j-3] == 'k' and S[i][j-4] == 'e':
            ret = []
            ret.append((i,j))
            ret.append((i,j-1))
            ret.append((i,j-2))
            ret.append((i,j-3))
            ret.append((i,j-4))
            return ret
        if i >= 4:
            # 左上
            if S[i-1][j-1] == 'n' and S[i-2][j-2] == 'u' and S[i-3][j-3] == 'k' and S[i-4][j-4] == 'e':
                ret = []
                ret.append((i,j))
                ret.append((i-1,j-1))
                ret.append((i-2,j-2))
                ret.append((i-3,j-3))
                ret.append((i-4,j-4))
                return ret
        if i <= H-5:
            # 左下
            if S[i+1][j-1] == 'n' and S[i+2][j-2] == 'u' and S[i+3][j-3] == 'k' and S[i+4][j-4] == 'e':
                ret = []
                ret.append((i,j))
                ret.append((i+1,j-1))
                ret.append((i+2,j-2))
                ret.append((i+3,j-3))
                ret.append((i+4,j-4))
                return ret
    # 上
    if i >= 4:
        if S[i-1][j] == 'n' and S[i-2][j] == 'u' and S[i-3][j] == 'k' and S[i-4][j] == 'e':
            ret = []
            ret.append((i,j))
            ret.append((i-1,j))
            ret.append((i-2,j))
            ret.append((i-3,j))
            ret.append((i-4,j))
            return ret
    # 下
    if i <= H-5:
        if S[i+1][j] == 'n' and S[i+2][j] == 'u' and S[i+3][j] == 'k' and S[i+4][j] == 'e':
            ret = []
            ret.append((i,j))
            ret.append((i+1,j))
            ret.append((i+2,j))
            ret.append((i+3,j))
            ret.append((i+4,j))
            return ret
    if j <= W-5:
        # 右
        if S[i][j+1] == 'n' and S[i][j+2] == 'u' and S[i][j+3] == 'k' and S[i][j+4] == 'e':
            ret = []
            ret.append((i,j))
            ret.append((i,j+1))
            ret.append((i,j+2))
            ret.append((i,j+3))
            ret.append((i,j+4))
            return ret
        if i >= 4:
            # 右上
            if S[i-1][j+1] == 'n' and S[i-2][j+2] == 'u' and S[i-3][j+3] == 'k' and S[i-4][j+4] == 'e':
                ret = []
                ret.append((i,j))
                ret.append((i-1,j+1))
                ret.append((i-2,j+2))
                ret.append((i-3,j+3))
                ret.append((i-4,j+4))
                return ret
        if i <= H-5:
            # 右下
            if S[i+1][j+1] == 'n' and S[i+2][j+2] == 'u' and S[i+3][j+3] == 'k' and S[i+4][j+4] == 'e':
                ret = []
                ret.append((i,j))
                ret.append((i+1,j+1))
                ret.append((i+2,j+2))
                ret.append((i+3,j+3))
                ret.append((i+4,j+4))
                return ret
    return []

ans = []
for i in range(H):
    for j in range(W):
        ch = S[i][j]
        if ch == 's':
            ans = check(i,j)
            if len(ans) != 0:
                break

    if len(ans) != 0:
        break

for elem in ans:
    print(elem[0]+1, elem[1]+1)