import sys
import heapq

INF = int(1e9)

n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(start, graph, n):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = [(0, start)]

    while queue:
        dist, now = heapq.heappop(queue)
        if dist > distance[now]:
            continue
        for neighbor, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))

    return distance

distance_from_1 = dijkstra(1, graph, n)
distance_from_v1 = dijkstra(v1, graph, n)
distance_from_v2 = dijkstra(v2, graph, n)

path1 = distance_from_1[v1] + distance_from_v1[v2] + distance_from_v2[n]
path2 = distance_from_1[v2] + distance_from_v2[v1] + distance_from_v1[n]

result = min(path1, path2)
print(result if result < INF else -1)