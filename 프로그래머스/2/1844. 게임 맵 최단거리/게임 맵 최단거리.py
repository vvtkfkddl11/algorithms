from collections import deque

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((0, 0))

    while queue:
        a, b = queue.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if a == n - 1 and b == m - 1:
            return visited[a][b]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[a][b] + 1
                queue.append((nx, ny))
    return -1
