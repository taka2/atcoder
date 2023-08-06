# -*- coding: utf-8 -*-
N = int(input())
AB = []
for i in range(N):
    A,B = map(int, input().split())
    AB.append((A,B))

sum = 0
for i in range(N):
    (A,B) = AB[i]
    sum += (A+B)*(B-A+1)//2

print(sum)