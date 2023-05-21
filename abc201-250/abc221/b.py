# -*- coding: utf-8 -*-
S = input()
T = input()

def exchangeChar(str, posa, posb):
    return str[:posa] + str[posb] + str[posa] + str[posb+1:]

if S == T:
    print("Yes")
    exit(0)

for i in range(len(S)-1):
    Sdash = exchangeChar(S, i, i+1)
    if Sdash == T:
        print("Yes")
        exit(0)

print("No")