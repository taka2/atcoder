# -*- coding: utf-8 -*-
S = input()
for i in range(len(S)-1,-1,-1):
    if S[i] == '.':
        print(S[(i+1):])
        break