# -*- coding: utf-8 -*-
n,m = map(int, input().split())
a = list(map(int, input().split()))
suma = []
sum = 0
for i in range(n):
    sum += a[i]
    suma.append(sum)

firstsum = 0
for i in range(m):
    firstsum += (i+1) * a[i]

max = None
prevsum = firstsum
for i in range(1, n-m+1):
    sum = prevsum
    #print(i,sum)
    sumaa = suma[i+m-2]
    sumab = 0
    if i-2>=0:
        sumab = suma[i-2]
    sum -= (sumaa - sumab)
    #print(i,sum)
    sum += m * a[i+m-1]
    #print(i,sum)
    prevsum = sum
    if max == None:
        max = sum
    elif sum > max:
        max = sum

if max == None:
    max = a[0]

print(max)
