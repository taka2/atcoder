# -*- coding: utf-8 -*-
n = int(input())
array = []
for i in range(n):
    array.append(input())

result = True
for i in range(n):
    for j in range(i+1, n):
        ir = array[i][j]
        jr = array[j][i]
        if not((ir=='W' and jr=='L') or (ir=='L' and jr=='W') or (ir=='D' and jr=='D')):
            result = False
            break

if(result):
    print("correct")
else:
    print("incorrect")