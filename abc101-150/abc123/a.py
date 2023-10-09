# -*- coding: utf-8 -*-
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

lista = [a,b,c,d,e]

ans = True
for i in range(4):
    for j in range(i+1,5):
        distance = abs(lista[i]-lista[j])
        if distance > k:
            ans = False
            break
    if not ans:
        break

if ans:
    print("Yay!")
else:
    print(":(")
