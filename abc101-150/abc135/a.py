# -*- coding: utf-8 -*-
A,B = map(int, input().split())

sum = A+B
if sum % 2 == 0:
    print(sum//2)
else:
    print("IMPOSSIBLE")