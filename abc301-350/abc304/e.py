# -*- coding: utf-8 -*-
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
   
N,M = map(int, input().split())
uv = []
for i in range(M):
    u,v = map(int, input().split())
    uv.append((u,v))

def getNewUnionFind():
    uf = UnionFind(N+1)
    for i in range(M):
        (u,v) = uv[i]
        uf.union(u,v)
    return uf

K = int(input())
xy = []
for i in range(K):
    (x,y) = map(int, input().split())
    xy.append((x,y))

Q = int(input())
pq = []
for i in range(Q):
    (p,q) = map(int, input().split())
    pq.append((p,q))

for i in range(Q):
    (p,q) = pq[i]
    uf = getNewUnionFind()
    uf.union(p,q)

    ans = True
    for i in range(K):
        (x,y) = xy[i]
        if uf.same(x,y):
            ans = False
            break
    
    if ans:
        print("Yes")
    else:
        print("No")
