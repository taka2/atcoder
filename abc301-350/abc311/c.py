# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10000000)
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

N = int(input())
A = [0] + list(map(int, input().split()))

chouten = -1
uf = UnionFind(N+1)
for i in range(1,N+1):
    a = i
    b = A[i]
    if uf.same(a,b):
        chouten = a
        break
    uf.union(a,b)

hen = defaultdict(list)
for i in range(1,N+1):
    hen[i].append(A[i])

def dfs(pos, route):
    for i in hen[pos]:
        if i in route:
            route[i] = 1
            return route
        else:
            route[i] = 1
            return dfs(i, route)

initialRoute = {chouten:1}
result = dfs(chouten, initialRoute)
print(len(result))
ansList = []
for i in result:
    ansList.append(i)
print(*ansList)