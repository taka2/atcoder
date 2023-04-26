# -*- coding: utf-8 -*-
from collections import deque

S = input()

stack = deque()
for i in range(len(S)):
    if S[i] == '(':
        stack.append(i+1)
    elif S[i] == ')':
        spoint = stack.pop()
        print(spoint,i+1)