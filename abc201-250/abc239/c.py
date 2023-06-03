# -*- coding: utf-8 -*-
x1,y1,x2,y2 = map(int, input().split())

directions = [(1,2), (2,1), (1,-2), (2,-1), (-1, -2), (-2, -1), (-1, 2), (-2, 1)]

ans = False
for dir1 in directions:
    for dir2 in directions:
        x1dash = x1 + dir1[0]
        y1dash = y1 + dir1[1]
        x2dash = x2 + dir2[0]
        y2dash = y2 + dir2[1]

        if x1dash == x2dash and y1dash == y2dash:
            ans = True
            break
    
    if ans:
        break

if ans:
    print("Yes")
else:
    print("No")