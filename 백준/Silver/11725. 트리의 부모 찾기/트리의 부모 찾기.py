import sys
from collections import deque


n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

# print(tree)

queue = deque([1])
visited = [False] * (n+1)
visited[1] = True
parents = [0] * (n+1)

while queue:
    x = queue.popleft()
    for nx in tree[x]:
        if not visited[nx]: # visited[x]가 아님을 주의
            parents[nx] = x
            visited[nx] = True
            queue.append(nx)

for i in range(2, n+1):
    print(parents[i])