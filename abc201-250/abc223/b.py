# -*- coding: utf-8 -*-
S = input()
min = S
max = S

for i in range(len(S)):
    Sdash = S[i:len(S)] + S[:i]
    if Sdash > max:
        max = Sdash
    if Sdash < min:
        min = Sdash

print(min)
print(max)