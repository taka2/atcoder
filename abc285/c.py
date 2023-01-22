# -*- coding: utf-8 -*-
S = input()
lenS = len(S)

ans = 0
for i in range(lenS):
    charIndex = lenS-i-1
    ch = S[charIndex]
    chOrd = ord(ch) - 64
    ans += chOrd * (26 ** i)

print(ans)