# -*- coding: utf-8 -*-
N,A,B = map(int, input().split())

# 行
for i in range(N):
    for a in range(A):
        S = ""
        if i % 2 == 0:
            color = False
        else:
            color = True
        # 列
        for j in range(N):
            if j != 0:
                color = not color
            for b in range(B):
                if color:
                    S += "#"
                else:
                    S += "."
        print(S)
