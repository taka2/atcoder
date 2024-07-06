# -*- coding: utf-8 -*-
N,S,K = map(int, input().split())
PQ = []

for i in range(N):
    (P,Q) = map(int, input().split())
    PQ.append((P,Q))

sum = 0
for i in range(N):
    (P,Q) = PQ[i]
    sum += P*Q

if sum < S:
    sum += K

print(sum)