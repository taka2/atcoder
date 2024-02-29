# -*- coding: utf-8 -*-
A = int(input())
B = int(input())
C = int(input())

lista = [A,B,C]
sortedList = sorted(lista, reverse=True)

print(sortedList.index(A)+1)
print(sortedList.index(B)+1)
print(sortedList.index(C)+1)