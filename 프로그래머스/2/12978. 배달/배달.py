# 23:15
import sys
from collections import deque
    
        
def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    visited = [sys.maxsize] * (N + 1)
    visited[1] = 0
    
    for a, b, c in road:
        
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    queue = deque([[1, 0]])

    # bfs
    while queue:

        target, num = queue.popleft()
        
        for j in graph[target]:
            if num + j[1] <= K and num + j[1] < visited[j[0]]:
                visited[j[0]] = num + j[1]
                queue.append([j[0], num + j[1]])

    
    for k in visited:
        if k != sys.maxsize:
            answer += 1

    return answer




# from collections import deque

# def solution(N, road, K):
#     answer = 0
#     graph = [[] for _ in range(N+1)]
#     visited = [0]*(N+1)
    
#     for i in road:
#         graph[i[0]].append(i[1])
#         graph[i[0]].append(i[2])
#         graph[i[1]].append(i[0])
#         graph[i[0]].append(i[2])
#     print(graph)
#     cnt = 0
    
#     def bfs(v):
#         queue = deque()
#         queue.append(v)
#         visited[v] = 1
#         while queue:
#             cur = queue.popleft()
#             for i in graph[cur]:
#                 if visited[i] == 0:
#                     visited[i] = 1
#                     print(graph[cur][2])
#                     if graph[cur][2] <= k:
#                         cnt+=1
    
#     bfs(0)
#     print(cnt)
    



#     return answer