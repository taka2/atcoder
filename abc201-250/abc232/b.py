# -*- coding: utf-8 -*-
S = input()
T = input()

def slide(S, slide):
    Sdash = ""
    for i in range(len(S)):
        ch = S[i]
        ordch = ord(ch)
        slidedch = ordch + (slide%26)
        if slidedch > 122:
            slidedch -= 26
        Sdash += chr(slidedch)
    return Sdash

ans = False
for i in range(26):
    Sdash = slide(S, i)
    if Sdash == T:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")