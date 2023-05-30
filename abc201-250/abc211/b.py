# -*- coding: utf-8 -*-
S1 = input()
S2 = input()
S3 = input()
S4 = input()

map = {}
map[S1] = 1
map[S2] = 1
map[S3] = 1
map[S4] = 1

if "H" in map and "2B" in map and "3B" in map and "HR" in map:
    print("Yes")
else:
    print("No")