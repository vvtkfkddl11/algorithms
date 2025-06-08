import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = [[-1]*m for _ in range(n)]

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            queue.append((i, j))
            result[i][j] = 0
        elif graph[i][j] == 0:
            result[i][j] = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and result[nx][ny] == -1:
            result[nx][ny] = result[x][y] + 1
            queue.append((nx, ny))

for i in result:
    print(*i)