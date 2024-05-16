# -*- coding: utf-8 -*-
N = int(input())
a = list(map(int, input().split()))

sortedA = sorted(a, reverse=True)

alice = 0
bob = 0
for i in range(N):
    if i % 2 == 0:
        alice += sortedA[i]
    else:
        bob += sortedA[i]

print(alice-bob)