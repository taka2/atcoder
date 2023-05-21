# -*- coding: utf-8 -*-
N = int(input())
X = list(map(int, input().split()))

sortedX = sorted(X)

trimmedX = sortedX[N:(5*N)-N]

sum = 0
for i in trimmedX:
    sum += i

print(sum / len(trimmedX))