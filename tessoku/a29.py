# -*- coding: utf-8 -*-
a,b = map(int, input().split())
modN = 10**9+7

def Power(a,b,m):
    p = a
    ans = 1

    for i in range(30):
        wari = 1 << i
        if (b // wari) % 2 == 1:
            ans = (ans * p) % m
        p = (p*p) % m
    
    return ans

print(Power(a,b,modN))