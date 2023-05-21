# -*- coding: utf-8 -*-
s = []
for i in range(10):
    s.append(input())

a=0
b=0
c=0
d=0
for i in range(10):
    cc = s[i].find('#')
    dd = s[i].rfind('#')
    if cc != -1:
        b = i+1
        c = cc+1
        d = dd+1
        if a == 0:
            a = i+1

print(a,b)
print(c,d)
    