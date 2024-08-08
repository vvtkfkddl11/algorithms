import sys
import heapq

INF = int(1e9)

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())  # u, v, w
    graph[a].append((b, c))


def dijkstra(k):
    q = []
    heapq.heappush(q, (0, k))
    distance[k] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(k)


for i in range(1, v+1):
    if distance[i] == INF:  # 경로가 존재하지 않음
        print("INF")
    else:
        print(distance[i])