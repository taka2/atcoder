# -*- coding: utf-8 -*-
import hashlib

N,Q = map(int, input().split())
S = " " + input()
for i in range(Q):
    a,b,c,d = map(int, input().split())
    #hasha = hashlib.md5(S[a:b+1].encode()).hexdigest()
    #hashb = hashlib.md5(S[c:d+1].encode()).hexdigest()
    #if hasha == hashb:
    if S[a:b+1] == S[c:d+1]:
        print("Yes")
    else:
        print("No")