# -*- coding: utf-8 -*-
AB,BC,CA = map(int, input().split())

sortedList = sorted([AB,BC,CA])

print(sortedList[0] * sortedList[1] // 2)