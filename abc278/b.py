# -*- coding: utf-8 -*-
def getABCD(h, m):
    if h > 9:
        a = h // 10
        b = h % 10
    else:
        a = 0
        b = h

    if m > 9:
        c = m // 10
        d = m % 10
    else:
        c = 0
        d = m
    
    return (a,b,c,d)

def judge(a,b,c,d):
    h = a*10+c
    m = b*10+d
    return (h >= 0 and h <= 23 and m >= 0 and m <= 59)

# 整数の入力
h, m = map(int, input().split())

while(True):
    (a,b,c,d) = getABCD(h,m)
    if(judge(a,b,c,d)):
        break

    m = m+1
    if m == 60:
        h = h+1
        m = 0
        if h == 24:
            h = 0
            m = 0

print(h,m)