import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def solution(n, m, x, y, graph):
    answer = 0
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    # 방문 배열을 초기화하고 시작 위치의 사탕 개수를 설정
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[x][y] = graph[x][y]
    for i in range(n):
        for j in range(m):
            for k in range(3):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < n and 0 <= y < m:
                    current = visited[i][j] + graph[x][y]
                    if visited[x][y] < current:
                        visited[x][y] = current
    answer = visited[n-1][m-1]
    return answer


print(solution(n, m, 0, 0, graph))