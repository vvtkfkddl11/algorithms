import sys

n = int(sys.stdin.readline())
target = int(sys.stdin.readline())

graph = [[0]*n for _ in range(n)]

# 하, 우, 상, 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = 0
# d=0 (dx[0],dy[0]) 일때 하
# d=1 (dx[1],dy[1]) 일때 우
# d=2 (dx[2],dy[2]) 일때 상
# d=3 (dx[3],dy[3]) 일때 좌

x, y = 0, 0
target_x, target_y = 0, 0
num = n*n

while num >= 1:
    graph[x][y] = num

    if num == target:
        target_x, target_y = x + 1, y + 1

    num -= 1

    nx = x + dx[d]
    ny = y + dy[d]

    # nx < 0 또는 nx >= n: x 좌표가 배열 범위를 벗어났는지 확인
    # ny < 0 또는 ny >= n: y 좌표가 배열 범위를 벗어났는지 확인
    # graph[nx][ny] != 0: 이미 숫자가 채워진 위치인지 확인
    if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] != 0:
        d = (d+1) % 4
        nx = x + dx[d]
        ny = y + dy[d]

    x, y = nx, ny

for i in range(n):
    for j in range(n):
        print(graph[i][j], end = " ")
    print()

print(target_x, target_y)