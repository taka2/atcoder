# -*- coding: utf-8 -*-
A = []
for i in range(3):
    A.append(list(map(int, input().split())))

N = int(input())
b = []
for i in range(N):
    b.append(int(input()))

checked = []
for i in range(3):
    checked.append([False, False, False])

for bi in range(N):
    bi = b[bi]
    for i in range(3):
        for j in range(3):
            if A[i][j] == bi:
                checked[i][j] = True

if checked[0][0] and checked[0][1] and checked[0][2]:
    print("Yes")
elif checked[1][0] and checked[1][1] and checked[1][2]:
    print("Yes")
elif checked[2][0] and checked[2][1] and checked[2][2]:
    print("Yes")
elif checked[0][0] and checked[1][0] and checked[2][0]:
    print("Yes")
elif checked[0][1] and checked[1][1] and checked[2][1]:
    print("Yes")
elif checked[0][2] and checked[1][2] and checked[2][2]:
    print("Yes")
elif checked[0][0] and checked[1][1] and checked[2][2]:
    print("Yes")
elif checked[2][0] and checked[1][1] and checked[0][2]:
    print("Yes")
else:
    print("No")