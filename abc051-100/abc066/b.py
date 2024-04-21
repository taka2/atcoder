# -*- coding: utf-8 -*-
def judge(str):
    if len(str) % 2 == 1:
        return False
    
    substrlen = len(str) // 2
    if str[0:substrlen] == str[substrlen:]:
        return True
    else:
        return False

S = input()
for i in range(1,len(S)-1):
    subS = S[0:len(S)-i]
    if judge(subS):
        print(len(subS))
        break
