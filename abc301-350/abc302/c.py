# -*- coding: utf-8 -*-
import itertools

N,M = map(int, input().split())
S = []
for i in range(N):
    S.append(input())

def check(s1, s2):
    diffcnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diffcnt += 1

    return diffcnt

ans = False
for elem in itertools.permutations(S, N):
    elemCheckResult = True
    for i in range(len(elem)-1):
        checkResult = check(elem[i], elem[i+1])
        if checkResult != 1:
            elemCheckResult = False
            break
    if elemCheckResult:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")