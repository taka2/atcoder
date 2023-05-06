# -*- coding: utf-8 -*-
K = int(input())
A,B = input().split()

def toDec(N,K):
    ans = 0
    for i in range(len(N)-1, -1, -1):
        a = int(N[i])
        ans += a * pow(K,len(N)-i-1)
    return ans

decA = toDec(A,K)
decB = toDec(B,K)
print(decA * decB)