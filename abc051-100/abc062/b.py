# -*- coding: utf-8 -*-
H,W = map(int, input().split())
a = []
for i in range(H):
    a.append(input())

line = ""
for i in range(W+2):
    line += "#"

print(line)
for i in range(H):
    print("#" + a[i] + "#")
print(line)