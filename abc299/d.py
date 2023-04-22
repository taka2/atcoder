# -*- coding: utf-8 -*-
N = int(input())

for i in range(2,min(N+1,12)):
    print("?",i)
    Si = int(input())
    if Si == 1:
        print("!",(i-1))
        exit(0)

for i in range(N-1,max(N-11,0),-1):
    print("?",i)
    Si = int(input())
    if Si == 0:
        print("!",i)
        exit(0)
