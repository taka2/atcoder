# -*- coding: utf-8 -*-
X = input()

X1 = int(X[0])
X2 = int(X[1])
X3 = int(X[2])
X4 = int(X[3])

if X1 == X2 and X2 == X3 and X3 == X4:
    print("Weak")
    exit(0)

if (X1+1)%10 == X2 and (X2+1)%10 == X3 and (X3+1)%10 == X4:
    print("Weak")
    exit(0)

print("Strong")