# -*- coding: utf-8 -*-
N = int(input())
S = input()

def getChars(s):
    mapS = {}
    for i in range(len(s)):
        if s[i] not in mapS:
            mapS[s[i]] = 1
    
    return mapS

ans = 0
for i in range(1,N):
    s1 = S[:i]
    s2 = S[i:]
    mapS1 = getChars(s1)
    mapS2 = getChars(s2)

    count = 0
    for ch in mapS1:
        if ch in mapS2:
            count += 1
    
    ans = max(ans, count)

print(ans)