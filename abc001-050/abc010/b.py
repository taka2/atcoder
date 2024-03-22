# -*- coding: utf-8 -*-
def judge(n):
    if n % 2 == 0:
        return False
    if (n+1) % 3 == 0:
        return False
    return True

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(3):
        if judge(a[i]):
            break
        else:
            a[i] -=1
            ans += 1

print(ans)