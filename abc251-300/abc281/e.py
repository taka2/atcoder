# -*- coding: utf-8 -*-
from collections import defaultdict

n,m,k = map(int, input().split())
a = list(map(int, input().split()))

def sum(countmap, k):
    #print(map, k)
    sortedKeys = sorted(countmap)
    #print(sortedKeys)

    sum = 0
    a = k
    for i in sortedKeys:
        count = countmap[i]
        if a > count:
            sum += i * count
            a -= count
        else:
            sum += i * a
            a = 0

        if a == 0:
            break
    return(sum)


countmap = defaultdict(int)
for i in range(m):
    countmap[a[i]] += 1

result = []
for i in range(n-m+1):
    if i != 0:
        countmap[a[i+m-1]] += 1
        countmap[a[i-1]] -= 1
        if countmap[a[i-1]] == 0:
            del countmap[a[i-1]]
    result.append(sum(countmap, k))

print(" ".join(map(str, result)))