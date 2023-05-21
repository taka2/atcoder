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

def count(fact):
    ans = 1
    for i in range(len(fact)):
        if fact[i][0] != 1:
            ans *= (fact[i][1]+1)
    return ans

N = int(input())
halfN = N//2

ans = 0
for i in range(1,N):
    a = i
    b = N-i
    facta = factorization(a)
    factb = factorization(b)
    ans = ans + count(facta) * count(factb)

print(ans)