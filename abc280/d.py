# -*- coding: utf-8 -*-
import math

def is_prime(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

k = int(input())

if is_prime(k):
    print(k)
    exit(0)

n = 1
while True:
    f = math.factorial(n)
    if f % k == 0:
        break
    n += 1

print(n)