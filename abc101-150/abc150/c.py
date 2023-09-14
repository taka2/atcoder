# -*- coding: utf-8 -*-
import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

order = 1
a = -1
b = -1
for elem in itertools.permutations(list(range(1,N+1))):
    if list(elem) == P:
        a = order
    if list(elem) == Q:
        b = order
    order += 1

print(abs(a-b))