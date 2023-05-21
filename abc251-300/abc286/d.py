# -*- coding: utf-8 -*-
N,X = map(int, input().split())
AB = []
for i in range(N):
    AB.append((map(int, input().split())))

map = {}
for i in range(N):
    (A,B) = AB[i]
    for j in range(B):
        amount = A*(j+1)
        if amount <= X:
            map[amount] = 1

def search(map, X):
    for i in map:
        if i == X:
            print(map,i,X)
            return True
        else:
            copymap = map.copy()
            del copymap[i]
            if X-i < 0:
                pass
            else:
                if search(copymap, X-i):
                    return True
    return False

ans = search(map, X)
print(ans)
