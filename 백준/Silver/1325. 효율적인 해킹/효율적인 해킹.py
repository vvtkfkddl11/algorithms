import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]  # graph = [] * (n+1) 아님
visited_cnt = []
answer = []
max_v = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b] += [a]


def bfs(node):
    global cnt
    q = deque()
    q.append(node)
    visited[node] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                cnt += 1
    return


for i in range(1, n+1):
    cnt = 0
    visited = [0] * (n+1)
    bfs(i)
    visited_cnt.append(cnt)

max_v = max(visited_cnt)

for i in range(len(visited_cnt)):
    if visited_cnt[i] == max_v:
        answer.append(i+1)

print(*answer)