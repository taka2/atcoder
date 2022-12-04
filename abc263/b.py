# -*- coding: utf-8 -*-
n = int(input())
p = list(map(int, input().split()))

current = n
dai = 0
while True:
    current = p[current - 2]
    dai += 1
    if current == 1:
        break

print(dai)