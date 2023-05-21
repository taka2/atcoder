# -*- coding: utf-8 -*-
from collections import defaultdict

N = int(input())
Q = int(input())

box = defaultdict(list)
number = defaultdict(list)

for i in range(Q):
    query = input().split()
    if query[0] == '1':
        i = int(query[1])
        j = int(query[2])
        box[j].append(i)
        if j not in number[i]:
            number[i].append(j)
    elif query[0] == '2':
        i = int(query[1])
        sortedi = sorted(box[i])
        print(*sortedi)
    elif query[0] == '3':
        i = int(query[1])
        sortedi = sorted(number[i])
        print(*sortedi)
