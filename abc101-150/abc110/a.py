# -*- coding: utf-8 -*-
A,B,C = map(int, input().split())

list = [A,B,C]
sortedList = sorted(list, reverse=True)

print(sortedList[0]*10 + sortedList[1] + sortedList[2])