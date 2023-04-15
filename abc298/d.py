# -*- coding: utf-8 -*-
Q = int(input())

S = [1]
index = 0

for i in range(Q):
    query = input().split()
    if query[0] == '1':
        x = query[1]
        S.append(int(x))
    elif query[0] == '2':
        index += 1
    elif query[0] == '3':
        slicedS = S[index:]
        value = 0
        keta = 1
        for i in range(len(slicedS)-1, -1, -1):
            value += int(slicedS[i]) * keta
            keta *= 10
        print(int(value % 998244353))