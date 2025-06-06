import heapq

def dijkstra(start, n):
    dist = [float('inf')]*(n+1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cost, temp = heapq.heappop(queue)
        if dist[temp] < cost:
            continue
        for i in range(1, n+1):
            if dist[i] > graph[temp][i] + cost:
                dist[i] = graph[temp][i] + cost
                heapq.heappush(queue, (dist[i], i))
    return dist
graph = [[float('inf')]*(201) for _ in range(201)]
def solution(n, s, a, b, fares):
    answer = float('inf')
    for x, y, c in fares:
        graph[x][y] = c
        graph[y][x] = c
    distance = dijkstra(s, n)
    for i in range(1, n+1):
        temp = dijkstra(i, n)
        answer = min(temp[a]+temp[b]+distance[i], answer)
    return answer