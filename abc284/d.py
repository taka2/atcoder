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

T = int(input())
for i in range(T):
    fact = factorization(int(input()))
    fact0 = fact[0]
    fact1 = fact[1]
    if fact0[1] == 2:
        print(fact0[0], fact1[0])
    else:
        print(fact1[0], fact0[0])

