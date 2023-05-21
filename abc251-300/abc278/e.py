# -*- coding: utf-8 -*-
H, W, N, h, w = map(int, input().split())
matrix = []
for i in range(H):
    matrix.append(list(map(int, input().split())))

def calc(basei,basej):
    #print("base=", basei, basej)
    resultMap = {}
    for i in range(H):
        for j in range(W):
            #print("zahyo=",i,j, basei+h-1, basej+w-1)
            if not (i >= basei and i <= (basei+h-1) and j >= basej and j <= (basej+w-1)):
                #print(i, j, matrix[i][j])
                resultMap[matrix[i][j]] = 1
    
    return(len(resultMap))

result = []
for i in range(H-h+1):
    resultRow = []
    for j in range(W-w+1):
        resultRow.append(calc(i,j))
    result.append(resultRow)

for i in range(len(result)):
    print(" ".join(map(str, result[i])))
        
