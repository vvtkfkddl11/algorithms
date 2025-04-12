import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
max_v = 0
visited_cnt = [0] * (n+1)
answer = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b] += [a]


def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = 1
    global cnt
    while queue:
        now_node = queue.popleft()
        for i in graph[now_node]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                queue.append(i)

    return


for i in range(1, n+1):
    visited = [0] * (n+1)
    cnt = 1
    bfs(i)
    visited_cnt[i] = cnt

max_v = max(visited_cnt)

for i in range(1, n+1):
    if visited_cnt[i] == max_v:
        answer.append(i)

print(*answer)