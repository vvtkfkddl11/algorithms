import sys
from collections import deque


n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
visited = [-1]*(n+1)
answer = []


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now_node = queue.popleft()
        for i in graph[now_node]:
            if visited[i] == -1:
                visited[i] = visited[now_node] + 1
                queue.append(i)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

bfs(x)

for i in range(n+1):
    if visited[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)