# -*- coding: utf-8 -*-
h,w = map(int, input().split())
count = 0
for i in range(h):
    count += input().count('#')

print(count)