# -*- coding: utf-8 -*-
from collections import deque

N,X = map(int, input().split())
A = [" "] + list(input())

queue = deque()
queue.append(X)
A[X] = '@'

while len(queue) > 0:
    pos = queue.popleft()
    if pos >= 2 and A[pos-1] == '.':
        A[pos-1] = '@'
        queue.append(pos-1)
    if pos <= (N-1) and A[pos+1] == '.':
        A[pos+1] = '@'
        queue.append(pos+1)

ans = ""
for ch in A[1:]:
    ans += ch
print(ans)