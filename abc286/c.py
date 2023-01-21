# -*- coding: utf-8 -*-
N,A,B = map(int, input().split())
S = input()

def hantei(S):
    count = 0
    for i in range(len(S)//2):
        if S[i] != S[len(S)-i-1]:
            count += 1
    return count

hoge = hantei(S)
while hoge != 0:
    pass