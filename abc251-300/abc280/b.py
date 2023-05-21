# -*- coding: utf-8 -*-
n = int(input())
s = list(map(int, input().split()))

total = 0
resultList = []
for i in range(n):
    elem = s[i] - total
    total = s[i]
    print(elem)