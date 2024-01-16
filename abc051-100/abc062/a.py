# -*- coding: utf-8 -*-
x,y = map(int, input().split())

group1 = [1,3,5,7,8,10,12]
group2 = [4,6,9,11]
group3 = [2]

if x in group1 and y in group1:
    print("Yes")
elif x in group2 and y in group2:
    print("Yes")
else:
    print("No")