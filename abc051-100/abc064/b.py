# -*- coding: utf-8 -*-
N = int(input())
a = list(map(int, input().split()))

sortedA = sorted(a)

print(sortedA[-1]-sortedA[0])