# -*- coding: utf-8 -*-
Q = int(input())

stack = []
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        stack.append(query[1])
    elif query[0] == '2':
        print(stack[len(stack)-1])
    else:
        stack.pop()