# -*- coding: utf-8 -*-
P,Q,R = map(int, input().split())

list = []
list.append(P)
list.append(Q)
list.append(R)

sortedList = sorted(list)

print(sortedList[0] + sortedList[1])