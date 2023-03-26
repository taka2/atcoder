# -*- coding: utf-8 -*-
N = int(input())
W = list(input().split())

ans = False
for i in range(N):
    if W[i] == "and":
        ans = True 
    if W[i] == "not":
        ans = True
    if W[i] == "that":
        ans = True
    if W[i] == "the":
        ans = True
    if W[i] == "you":
        ans = True

if ans:
    print("Yes")
else:
    print("No")