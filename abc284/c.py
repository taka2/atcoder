# -*- coding: utf-8 -*-
N,M = map(int, input().split())
V = []
for i in range(M):
    v1,v2 = map(int, input().split())
    V.append((v1,v2))

list = []
for i in range(N):
    list.append([i+1])

for i in range(M):
    (v1,v2) = V[i]
    newlist = []
    for j in range(len(list)):
        if v1 in list[j]:
            v1list = list[j]
            newlist.extend(list[j])
        if v2 in list[j]:
            v2list = list[j]
            newlist.extend(list[j])
    if v1list != v2list:
        list.remove(v1list)
        list.remove(v2list)
        list.append(newlist)

print(len(list))