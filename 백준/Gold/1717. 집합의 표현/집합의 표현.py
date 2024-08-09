import sys
sys.setrecursionlimit(100_000)


# 잡합의 개수-1, 연산의 개수
n, m = map(int, sys.stdin.readline().split())
# parent = []
parent = [i for i in range(n+1)]


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    parent[parent_a] = parent_b


for i in range(m):
    num, a, b = map(int, sys.stdin.readline().split())
    if num == 0:
        union(a, b)
    else:
        if find(a) == find(b):
           print("YES")
        else:
            print("NO")