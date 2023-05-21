# -*- coding: utf-8 -*-
H,W = map(int, input().split())
R,C = map(int, input().split())

adjacent = 0
# up
if R != 1:
    adjacent += 1
# down
if R != H:
    adjacent += 1
# left
if C != 1:
    adjacent += 1
# right
if C != W:
    adjacent += 1
print(adjacent)