# -*- coding: utf-8 -*-
import heapq

Q = int(input())

priorityQueue = []
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        heapq.heappush(priorityQueue, int(query[1]))
    elif query[0] == '2':
        x = heapq.heappop(priorityQueue)
        print(x)
        heapq.heappush(priorityQueue,x)
    else:
        heapq.heappop(priorityQueue)