# -*- coding: utf-8 -*-
N = int(input())
S = input()

location = {(0,0):1}
current = (0,0)

ans = False
for i in range(N):
    if S[i] == 'R':
        current = (current[0]+1, current[1])
    if S[i] == 'L':
        current = (current[0]-1, current[1])
    if S[i] == 'U':
        current = (current[0], current[1]-1)
    if S[i] == 'D':
        current = (current[0], current[1]+1)
    
    if current in location:
        ans = True
        break
    else:
        location[current] = 1

if ans:
    print("Yes")
else:
    print("No")