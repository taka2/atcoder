# -*- coding: utf-8 -*-
N = int(input())

list = {1:1}
print(1)

for i in range(N+1):
    aoki = int(input())
    if aoki == 0:
        break

    list[aoki] = 1
    flag = False
    for j in range(1,(N*2)+2):
        if j not in list:
            flag = True
            list[j] = 1
            print(j)
            break
    if not flag:
        break
