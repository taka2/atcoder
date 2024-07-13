# -*- coding: utf-8 -*-
S = input()

if S[0] != '<':
    print("No")
    exit(0)

if S[-1] != '>':
    print("No")
    exit(0)

for i in range(1,len(S)-1):
    if S[i] != '=':
        print("No")
        exit(0)

print("Yes")