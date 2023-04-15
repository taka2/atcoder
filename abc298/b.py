# -*- coding: utf-8 -*-
N = int(input())

def rotate(arr):
    copyarr = []
    for i in range(N+1):
        copyarr.append([0]*(N+1))

    for i in range(1,N+1):
        for j in range(1,N+1):
            copyarr[i][j] = arr[N+1-j][i]
    return copyarr

def judge(A, B):
    ret = True
    for i in range(1, N+1):
        for j in range(1, N+1):
            if A[i][j] == 1 and B[i][j] == 0:
                ret = False
                break
        if ret == False:
            break
    return ret

A = [[0]*(N+1)]
for i in range(N):
    A.append([0] + list(map(int, input().split())))

B = [[0]*(N+1)]
for i in range(N):
    B.append([0] + list(map(int, input().split())))

rotate1 = rotate(A)
rotate2 = rotate(rotate1)
rotate3 = rotate(rotate2)

if judge(A,B) or judge(rotate1,B) or judge(rotate2,B) or judge(rotate3,B):
    print("Yes")
else:
    print("No")