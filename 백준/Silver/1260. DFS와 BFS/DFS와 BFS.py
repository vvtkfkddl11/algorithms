import sys
from collections import deque

dfs_answer = []
bfs_answer = []

n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n+1)]  # 그냥 [] 하니 범위 에러

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]
    # graph[a].append(b)
    # graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()


def dfs(x):
    dfs_visited[x] = True
    dfs_answer.append(x)
    for nx in graph[x]:
        if not dfs_visited[nx]:
            # dfs_visited[nx] = True
            dfs(nx)


def bfs(x):
    queue = deque([x])
    bfs_visited[x] = True
    while queue:
        x = queue.popleft()
        bfs_answer.append(x)
        for nx in graph[x]:
            if not bfs_visited[nx]:
                bfs_visited[nx] = True
                queue.append(nx)

dfs(v)
bfs(v)

print(*dfs_answer)
print(*bfs_answer)