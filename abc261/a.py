# -*- coding: utf-8 -*-
l1,r1,l2,r2 = map(int,(input().split()))

count = 0
for i in range(101):
    if i >= l1 and i <= r1 and i >= l2 and i <= r2:
        count += 1

if(count > 0):
    print(count-1)
else:
    print(count)