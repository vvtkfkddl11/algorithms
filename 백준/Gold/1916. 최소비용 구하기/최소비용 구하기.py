import sys
import heapq

INF = float('inf')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    s, e, cost = map(int, sys.stdin.readline().split())
    graph[s].append((e, cost))

start, end = map(int, sys.stdin.readline().split())
answer = 0

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(start)


print(distance[end])