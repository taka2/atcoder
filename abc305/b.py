# -*- coding: utf-8 -*-
p,q = input().split()
map = {}
map['A'] = 0
map['B'] = 3
map['C'] = 4
map['D'] = 8
map['E'] = 9
map['F'] = 14
map['G'] = 23

print(abs(map[q] - map[p]))