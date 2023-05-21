# -*- coding: utf-8 -*-
N,X = map(int, input().split())
A = [0] + list(map(int, input().split()))

set = {X}
current = X
while True:
    tell = A[current]
    if tell in set:
        break
    else:
        set.add(tell)
        current = tell

print(len(set))