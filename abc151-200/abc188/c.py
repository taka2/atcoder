# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

listA = []
for i in range(2**N):
    number = i+1
    rate = A[i]
    listA.append((number, rate))

def judge(arr):
    result = []
    for i in range(0,len(arr),2):
        p1 = arr[i]
        p2 = arr[i+1]
        if p1[1] > p2[1]:
            result.append(p1)
        else:
            result.append(p2)
    return result

Adash = listA
for i in range(N-1):
    Adash = judge(Adash)

p1 = Adash[0]
p2 = Adash[1]
if p1[1] > p2[1]:
    print(p2[0])
else:
    print(p1[0])