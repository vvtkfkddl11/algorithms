import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

candidates = []
for i in range(1, n-1):
    for j in range(1, n-1):
        candidates.append((i, j))

min_cost = float('inf')

for comb in combinations(candidates, 3):
    visited = [[False]*n for _ in range(n)]
    total = 0
    is_valid = True

    for x, y in comb:
        temp_cost = 0
        temp_positions = []

        for k in range(5):
            nx = x + dx[k]
            ny = y + dy[k]

            if visited[nx][ny]:
                is_valid = False
                break
            temp_cost += grid[nx][ny]
            temp_positions.append((nx, ny))

        if not is_valid:
            break

        for nx, ny in temp_positions:
            visited[nx][ny] = True
        total += temp_cost

    if is_valid:
        min_cost = min(min_cost, total)

print(min_cost)