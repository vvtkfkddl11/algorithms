import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())  # 노드, 엣지 개수
graph = [[] for _ in range(n+1)]
answer = [0]*(n+1)
max_value = 0


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        now_node = queue.popleft()
        for i in graph[now_node]:
            if visited[i] == 0:
                answer[i] += 1
                visited[i] = 1
                queue.append(i)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

for i in range(1, n+1):
    visited = [0]*(n+1)
    bfs(i)

for i in range(1, n+1):
    max_value = max(max_value, answer[i])

for i in range(1, n+1):
    if answer[i] == max_value:
        print(i)