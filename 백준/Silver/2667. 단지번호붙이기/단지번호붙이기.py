from collections import deque
import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]


def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1

    while queue:
        a, b = queue.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
                graph[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))
    return cnt

city_count = 0
answer = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            city_count += 1
            answer.append(bfs(i, j))

answer.sort()

print(city_count)
for count in answer:
    print(count)