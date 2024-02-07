# -*- coding: utf-8 -*-
n,x = map(int, input().split())

left = x-1
right = n-x
print(min(left, right))