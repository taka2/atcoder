# -*- coding: utf-8 -*-
S = input()
T = ""
for i in range(len(S)):
    if S[i] == '0':
        T += '1'
    else:
        T += '0'
    
print(T)