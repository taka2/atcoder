# -*- coding: utf-8 -*-
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

mod10A = A % 10
mod10B = B % 10
mod10C = C % 10
mod10D = D % 10
mod10E = E % 10

listmod10 = []
if mod10A != 0:
    listmod10.append(mod10A)
if mod10B != 0:
    listmod10.append(mod10B)
if mod10C != 0:
    listmod10.append(mod10C)
if mod10D != 0:
    listmod10.append(mod10D)
if mod10E != 0:
    listmod10.append(mod10E)

if len(listmod10) != 0:
    minmod10 = min(listmod10)
else:
    minmod10 = -1

def adjust(num):
    if num % 10 == 0:
        return num
    else:
        return num//10*10 + 10

ans = 0
if minmod10 == mod10A:
    ans += A
    ans += adjust(B)
    ans += adjust(C)
    ans += adjust(D)
    ans += adjust(E)
elif minmod10 == mod10B:
    ans += B
    ans += adjust(A)
    ans += adjust(C)
    ans += adjust(D)
    ans += adjust(E)
elif minmod10 == mod10C:
    ans += C
    ans += adjust(A)
    ans += adjust(B)
    ans += adjust(D)
    ans += adjust(E)
elif minmod10 == mod10D:
    ans += D
    ans += adjust(A)
    ans += adjust(B)
    ans += adjust(C)
    ans += adjust(E)
elif minmod10 == mod10E:
    ans += E
    ans += adjust(A)
    ans += adjust(B)
    ans += adjust(C)
    ans += adjust(D)
else:
    ans += A
    ans += B
    ans += C
    ans += D
    ans += E

print(ans)