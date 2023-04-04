# -*- coding: utf-8 -*-
n,r = map(int, input().split())
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

# 分子の計算
a = 1
for i in range(1,n+1):
    a *= i
    a %= modN

# 分母の計算
b = 1
for i in range(1,r+1):
    b *= i
    b %= modN

for i in range(1,n-r+1):
    b *= i
    b %= modN

# 割り算
ans = (a * Power(b, modN-2, modN)) % modN
print(ans)