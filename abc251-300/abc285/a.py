# -*- coding: utf-8 -*-
A,B = map(int, input().split())

con = {}
con[1] = [2,3]
con[2] = [1,4,5]
con[3] = [1,6,7]
con[4] = [2,8,9]
con[5] = [2,10,11]
con[6] = [3,12,13]
con[7] = [3,14,15]
con[8] = [4]
con[9] = [4]
con[10] = [5]
con[11] = [5]
con[12] = [6]
con[13] = [6]
con[14] = [7]
con[15] = [7]

if B in con[A]:
    print("Yes")
else:
    print("No")