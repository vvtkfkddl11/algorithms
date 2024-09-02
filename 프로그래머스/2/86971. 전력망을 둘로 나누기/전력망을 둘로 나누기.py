def solution(n, wires):
    answer = -1
    graph = [[] for _ in range(n+1)]
    min_v = float('inf')
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    print(graph)
    
    def dfs(node):
        cnt = 1
        visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                cnt += dfs(i)
        return cnt
    
    for a, b in wires:
        visited = [0]*(n+1)
        graph[a].remove(b)
        graph[b].remove(a)
        cnta = dfs(a)
        cntb = n - cnta
        graph[a].append(b)
        graph[b].append(a)
        min_v = min(min_v, abs(cnta-cntb))
        
    return min_v