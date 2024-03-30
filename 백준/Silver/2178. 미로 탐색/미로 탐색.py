from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]


def solution(x, y, maze):
    result = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue = deque()
    queue.append((x, y))
    while queue:
        node = queue.popleft()
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[node[0]][node[1]] + 1
                    queue.append((nx, ny))
    result = maze[N-1][M-1]
    return result


print(solution(0, 0, maze))