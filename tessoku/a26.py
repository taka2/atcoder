# -*- coding: utf-8 -*-
import math

def isPrime(X):
    to = int(math.sqrt(X))
    for i in range(2, to+1):
        if X % i == 0:
            return False
    return True

Q = int(input())
for i in range(Q):
    X = int(input())
    if isPrime(X):
        print("Yes")
    else:
        print("No")