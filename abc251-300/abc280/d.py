# -*- coding: utf-8 -*-
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

k = int(input())
fact = factorization(k)

def f(n,p):
    if n == 0:
        return 0
    n = n // p
    return n + f(n,p)

ac=k
wa=0
while(ac-wa > 1):
    wj = (ac+wa)//2
    ok = True
    for elem in fact:
        p = elem[0]
        cnt = elem[1]
        if(f(wj,p) < cnt):
            ok = False
    if ok:
        ac = wj
    else:
        wa = wj

print(ac)