from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(x, y, d):
    result = 0
    global cnt
    need_visited = deque()
    need_visited.append((x, y))  # 로봇의 현위치 (r, c)
    visited[x][y] = 1
    cnt += 1

    while need_visited:
        node = need_visited.popleft()
        flag = 0
        for _ in range(4):  # 반시계 방향으로 돌려감
            d = (d + 3) % 4
            nx = node[0] + dx[d]
            ny = node[1] + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not grid[nx][ny]:  # grid가 0일때(청소할 곳O)
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    need_visited.append((nx, ny))
                    cnt += 1
                    flag = 1  # 빈칸이 있을 때 = 청소할 공간이 있을 때
                    break
        if flag == 0:  # 빈칸이 없을 때 -> 후진
            if grid[node[0] - dx[d]][node[1] - dy[d]] != 1:
                need_visited.append((node[0] - dx[d], node[1] - dy[d]))
            else:  # 1일 때 (청소할 곳X)
                print(cnt)
                break


solution(r, c, d)