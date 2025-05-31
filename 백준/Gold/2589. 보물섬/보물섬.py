import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    queue = deque()
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])
                queue.append((nx, ny))
    return cnt - 1


max_v = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            max_v = max(max_v, bfs(i, j))

print(max_v)