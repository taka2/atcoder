# -*- coding: utf-8 -*-
def countSharp(s):
    return s.count('#')

H,W = map(int, input().split())
S = []
T = []

for i in range(H):
    S.append(input())
for j in range(H):
    T.append(input())

result = True
for i in range(H):
    if countSharp(S[i]) != countSharp(T[i]):
        result = False
        break

if(result):
    print("Yes")
else:
    print("No")