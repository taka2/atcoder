# -*- coding: utf-8 -*-
S1 = input()
S2 = input()
S3 = input()

map = {}
map[S1] = 1
map[S2] = 1
map[S3] = 1

list = ["ABC", "ARC", "AGC", "AHC"]
for elem in list:
    if elem not in map:
        print(elem)