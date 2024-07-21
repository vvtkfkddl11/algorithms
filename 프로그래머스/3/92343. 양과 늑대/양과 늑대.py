def solution(info, edges):
    answer = []
    visited = [0] * len(info)
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else: 
            return 
        
        for a, b in edges:
            if visited[a] and not visited[b]:
                visited[b] = 1
                if info[b] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[b] = 0
        
    visited[0] = 1
    dfs(1, 0)
    
    return max(answer)