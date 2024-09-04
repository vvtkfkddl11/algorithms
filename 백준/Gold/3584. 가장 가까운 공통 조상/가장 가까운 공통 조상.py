import sys
from collections import defaultdict

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    tree = defaultdict(list)
    for j in range(n-1):
        parent, child = map(int, sys.stdin.readline().split())
        tree[child] = parent
    a, b = map(int, sys.stdin.readline().split())
    a_parents = []
    while a in tree:
        a_parents.append(a)
        a = tree[a]
    while b in tree:
        if b in a_parents:
            break
        b = tree[b]
    print(b)