# -*- coding: utf-8 -*-
N,M = map(int, input().split())

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

def check(X):
    fact = factorization(X)
    if len(fact) == 2 and fact[0][1] == 1 and fact[1][1] == 1:
        return True
    else:
        return False

#left = M, right = N**2
#while left < right:
#    mid = (left + right) // 2
#    ans = check(mid)

fact = factorization(16)
print(fact)

ans = -1
for X in range(M, N**2+1):
    for a in range(1,N+1):
        if X%a == 0 and X//a <= N:
            ans = X
            break
    if ans != -1:
        break

print(ans)