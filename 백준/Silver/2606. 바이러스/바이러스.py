import sys

answer = 0
n = int(sys.stdin.readline())
n_pairs = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)

for i in range(n_pairs):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    visited[node] = 1
    for nx in graph[node]:
        if visited[nx] == 0:
            dfs(nx)


dfs(1)
# print(visited)
answer = sum(visited)-1
print(answer)
