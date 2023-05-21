# -*- coding: utf-8 -*-
S = input()

def lswap(S, index, ch):
    tmp = S[index-1]
    return S.replace(ch, 'x').replace(tmp, ch).replace('x', tmp)

def rswap(S, index, ch):
    tmp = S[index+1]
    return S.replace(ch, 'x').replace(tmp, ch).replace('x', tmp)

count = 0

aindex = S.index('a')
while S[0] != 'a':
    for i in range(aindex, 0, -1):
        S = lswap(S, i, 'a')
        #print("swapa", S, i)
        count += 1

tindex = S.index('t')
while S[1] != 't':
    if tindex > 1:
        for i in range(tindex, 1, -1):
            S = lswap(S, i, 't')
            #print("swaptl", S, i)
            count += 1
    else:
        for i in range(1):
            S = rswap(S, i, 't')
            #print("swaptr", S, i)
            count += 1

cindex = S.index('c')
while S[2] != 'c':
    if cindex > 2:
        for i in range(cindex, 2, -1):
            S = lswap(S, i, 'c')
            #print("swapcl", S, i)
            count += 1
    else:
        for i in range(2):
            S = rswap(S, i, 'c')
            #print("swapcr", S, i)
            count += 1

oindex = S.index('o')
while S[3] != 'o':
    if oindex > 3:
        for i in range(oindex, 3, -1):
            S = lswap(S, i, 'o')
            #print("swapol", S, i)
            count += 1
    else:
        for i in range(3):
            S = rswap(S, i, 'o')
            #print("swapor", S, i)
            count += 1

dindex = S.index('d')
while S[4] != 'd':
    if dindex > 4:
        for i in range(dindex, 4, -1):
            S = lswap(S, i, 'd')
            #print("swapdl", S, i)
            count += 1
    else:
        for i in range(4):
            S = rswap(S, i, 'd')
            #print("swapdr", S, i)
            count += 1

eindex = S.index('e')
while S[5] != 'e':
    if eindex > 5:
        for i in range(eindex, 5, -1):
            S = lswap(S, i, 'e')
            #print("swapel", S, i)
            count += 1
    else:
        for i in range(5):
            S = rswap(S, i, 'e')
            #print("swaper", S, i)
            count += 1

print(count)