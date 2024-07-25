# 최단 거리 -> bfs

from collections import deque 

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    # visited = [0] * len(maps) for _ in len(maps[0])
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        a, b = queue.popleft()
        # if 도달
        if a == n-1 and b == m-1:
            return visited[a][b]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
        # 벽이면
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif maps[nx][ny] == 1 and visited[nx][ny] == 0:
                # visited[nx][ny] == 1
                visited[nx][ny] = visited[a][b] + 1
                queue.append((nx, ny))
            
    return -1