# -*- coding: utf-8 -*-
import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
lr = []
for i in range(Q):
    l,r = map(int, input().split())
    lr.append((l,r))

sumA = []
keysA = []
prev = 0
prevSum = 0
for i in range(N):
    if i == 0:
        # 0は無視
        pass
    elif i % 2 == 1:
        # 奇数は値を保存
        prev = A[i]
        #print("prev=",prev)
    else:
        # 偶数は睡眠時間を保存
        sum = A[i]-prev
        #print("sum=", sum, "prevsum=", prevSum)
        keysA.append(A[i-1])
        sumA.append((A[i-1], A[i], sum+prevSum))
        prevSum = sum+prevSum
    
#print(sumA)
#print(bisect.bisect_left(keysA, 1200))

for i in range(Q):
    (l,r) = lr[i]
    lsumAIndex = bisect.bisect_left(keysA, l)
    rsumAIndex = bisect.bisect_left(keysA, r)

    lminus = 0
    if lsumAIndex != 0:
        (lstart,lend,lsum) = sumA[lsumAIndex-1]
        if l>=lstart and l<=lend:
            lminus = lsum-(lend-l)
        else:
            lminus = lsum
    rplus = 0
    if rsumAIndex != 0:
        (rstart,rend,rsum) = sumA[rsumAIndex-1]
        if r>=rstart and r<=rend:
            rplus = rsum-(rend-rstart)+(r-rstart)
        else:
            rplus = rsum
    ans = rplus - lminus
    print(ans)