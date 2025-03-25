import sys

answer = 0
n = int(sys.stdin.readline())
n_pairs = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
# graph = [[0]*2 for i in range(n_pairs)]

for i in range(n_pairs):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []


def dfs(node):
    for connected_node in graph[node]:
        if connected_node not in visited:
            visited.append(connected_node)
            dfs(connected_node)


visited.append(1)
dfs(1)

answer = len(visited) - 1
print(answer)